from __future__ import annotations

import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple

import numpy as np
from rich.console import Console
from rich.panel import Panel

from vector_store import Embedder, load_index, load_chunks_jsonl
from citations import format_hit, format_ref

console = Console()


def search(
    query_vec: np.ndarray,
    index_or_vectors: Any,
    *,
    top_k: int,
    use_faiss: bool,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Returns (scores, idx)
    - scores shape: (top_k,)
    - idx shape: (top_k,)
    """
    if use_faiss:
        # faiss expects shape (n, dim)
        scores, idx = index_or_vectors.search(query_vec[None, :], top_k)
        return scores[0], idx[0]

    # brute-force cosine via dot product (since vectors are normalized)
    vectors = index_or_vectors
    scores_all = vectors @ query_vec  # (N,)
    if top_k >= len(scores_all):
        idx = np.argsort(-scores_all)
    else:
        idx = np.argpartition(-scores_all, top_k)[:top_k]
        idx = idx[np.argsort(-scores_all[idx])]
    return scores_all[idx], idx


def template_answer(hits: List[Tuple[float, Dict[str, Any]]], *, max_chars_each: int = 260) -> str:
    lines = []
    lines.append("根据检索到的资料片段，整理要点如下（每条均附引用）：")
    for score, c in hits:
        snippet = c["text"].strip().replace("\n", " ")
        if len(snippet) > max_chars_each:
            snippet = snippet[: max_chars_each - 1] + "…"
        lines.append(f"- {snippet} {format_ref(c)}")
    lines.append("")
    lines.append("提示：以上为“模板式拼接”结果，适合验证检索与引用链路；后续如接入大模型生成，可在此基础上做摘要与融合。")
    return "\n".join(lines)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        raise SystemExit("Usage: python -m src.query --index_dir .rag_index \"你的问题\"")

    ap = argparse.ArgumentParser()
    ap.add_argument("--index_dir", type=str, required=True)
    ap.add_argument("--top_k", type=int, default=5)
    ap.add_argument("--model", type=str, default=None)
    ap.add_argument("question", type=str)
    args = ap.parse_args()

    index_dir = Path(args.index_dir)
    chunks = load_chunks_jsonl(index_dir / "chunks.jsonl")
    index_or_vectors, use_faiss = load_index(index_dir)

    embedder = Embedder(model_name=args.model) if args.model else Embedder()
    qvec = embedder.embed([args.question])[0]

    scores, idx = search(qvec, index_or_vectors, top_k=args.top_k, use_faiss=use_faiss)

    hits: List[Tuple[float, Dict[str, Any]]] = []
    for s, i in zip(scores.tolist(), idx.tolist()):
        if i < 0:
            continue
        c = chunks[i]
        hits.append((float(s), c))

    console.print(Panel.fit(f"[b]Q:[/b] {args.question}\nuse_faiss={use_faiss} top_k={args.top_k}", title="Query"))
    console.print("[b]TopK Hits[/b]")
    for r, (s, c) in enumerate(hits, start=1):
        console.print(format_hit(r, s, c))

    console.print()
    console.print(Panel(template_answer(hits), title="Template Answer"))
