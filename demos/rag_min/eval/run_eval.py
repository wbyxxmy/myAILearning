from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, Any, List

import numpy as np

# Make src importable without packaging demos/ as a python package
BASE = Path(__file__).resolve().parent.parent
SRC = BASE / "src"
sys.path.insert(0, str(SRC))

from vector_store import Embedder, load_index, load_chunks_jsonl  # noqa: E402


def recall_at_k(hits_sources: List[str], expected_sources: List[str]) -> float:
    expected = set(expected_sources)
    got = set(hits_sources)
    return 1.0 if (expected & got) else 0.0


def main() -> None:
    index_dir = BASE / ".rag_index"
    qpath = Path(__file__).resolve().parent / "questions.jsonl"

    chunks = load_chunks_jsonl(index_dir / "chunks.jsonl")
    index_or_vectors, use_faiss = load_index(index_dir)

    embedder = Embedder()

    total = 0
    hit = 0

    for line in qpath.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        obj: Dict[str, Any] = json.loads(line)
        q = obj["question"]
        expected = obj["expected_sources"]
        k = int(obj.get("k", 5))

        qvec = embedder.embed([q])[0]

        if use_faiss:
            scores, idx = index_or_vectors.search(qvec[None, :], k)
            idx = idx[0].tolist()
        else:
            vecs = index_or_vectors
            scores_all = vecs @ qvec
            idx = np.argsort(-scores_all)[:k].tolist()

        sources = [chunks[i]["source_path"] for i in idx if i >= 0]
        r = recall_at_k(sources, expected)
        total += 1
        hit += int(r)

        print(f"Q: {q}")
        print(f" expected={expected} got_topk={sources}")
        print(f" recall@{k}={r:.1f}")
        print("-" * 60)

    print(f"Overall recall={hit}/{total}={hit/total if total else 0:.3f} use_faiss={use_faiss}")


if __name__ == "__main__":
    main()