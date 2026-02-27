from __future__ import annotations

import argparse
from pathlib import Path
from typing import List, Dict, Any

from chunking import chunk_markdown
from vector_store import Embedder, build_index, save_index, save_chunks_jsonl


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs_dir", type=str, required=True, help="Markdown 文档目录（如 data/docs）")
    ap.add_argument("--out_dir", type=str, required=True, help="索引输出目录（如 .rag_index）")
    ap.add_argument("--no_faiss", action="store_true", help="不使用 FAISS，改用 numpy 暴力检索")
    ap.add_argument("--model", type=str, default=None, help="sentence-transformers 模型名（可选）")
    ap.add_argument("--target_chars", type=int, default=1200)
    ap.add_argument("--overlap_chars", type=int, default=150)
    args = ap.parse_args()

    docs_dir = Path(args.docs_dir)
    out_dir = Path(args.out_dir)
    use_faiss = not args.no_faiss

    md_files = sorted(list(docs_dir.glob("**/*.md")))
    if not md_files:
        raise SystemExit(f"未找到 md 文件：{docs_dir}")

    all_chunks: List[Dict[str, Any]] = []
    for p in md_files:
        text = read_text(p)
        chunks = chunk_markdown(
            source_path=str(p.relative_to(docs_dir)).replace("\\", "/"),
            text=text,
            target_chars=args.target_chars,
            overlap_chars=args.overlap_chars,
        )
        for c in chunks:
            all_chunks.append(
                {
                    "chunk_id": c.chunk_id,
                    "source_path": c.source_path,
                    "title_path": c.title_path,
                    "text": c.text,
                }
            )

    embedder = Embedder(model_name=args.model) if args.model else Embedder()
    vectors = embedder.embed([c["text"] for c in all_chunks])

    index = build_index(vectors, use_faiss=use_faiss)

    out_dir.mkdir(parents=True, exist_ok=True)
    save_index(index, out_dir, use_faiss=use_faiss)
    save_chunks_jsonl(all_chunks, out_dir / "chunks.jsonl")

    print(f"[OK] docs={len(md_files)} chunks={len(all_chunks)} use_faiss={use_faiss} out={out_dir}")


if __name__ == "__main__":
    main()
