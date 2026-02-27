from __future__ import annotations

from pathlib import Path
from typing import List, Dict, Any, Tuple

import json
import numpy as np
from sentence_transformers import SentenceTransformer

try:
    import faiss  # type: ignore
except Exception:  # pragma: no cover
    faiss = None


DEFAULT_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


def _l2_normalize(x: np.ndarray) -> np.ndarray:
    denom = np.linalg.norm(x, axis=1, keepdims=True) + 1e-12
    return x / denom


class Embedder:
    def __init__(self, model_name: str = DEFAULT_MODEL):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts: List[str]) -> np.ndarray:
        vecs = self.model.encode(texts, show_progress_bar=True, normalize_embeddings=False)
        vecs = np.asarray(vecs, dtype="float32")
        return _l2_normalize(vecs)


def save_chunks_jsonl(chunks: List[Dict[str, Any]], path: Path) -> None:
    with path.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")


def load_chunks_jsonl(path: Path) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            out.append(json.loads(line))
    return out


def build_index(vectors: np.ndarray, *, use_faiss: bool) -> Any:
    if use_faiss:
        if faiss is None:
            raise RuntimeError("faiss 不可用：请安装 faiss-cpu 或改用 --no_faiss")
        dim = vectors.shape[1]
        index = faiss.IndexFlatIP(dim)  # cosine via normalized vectors
        index.add(vectors)
        return index
    # store vectors directly for brute-force search
    return vectors


def save_index(index: Any, out_dir: Path, *, use_faiss: bool) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    if use_faiss:
        if faiss is None:
            raise RuntimeError("faiss 不可用，无法保存 FAISS index")
        faiss.write_index(index, str(out_dir / "index.faiss"))
    else:
        np.save(out_dir / "vectors.npy", index)


def load_index(index_dir: Path) -> Tuple[Any, bool]:
    """
    Returns (index_or_vectors, use_faiss)
    - If index.faiss exists -> FAISS
    - Else vectors.npy -> brute-force
    """
    faiss_path = index_dir / "index.faiss"
    npy_path = index_dir / "vectors.npy"

    if faiss_path.exists():
        if faiss is None:
            raise RuntimeError("发现 index.faiss，但当前环境未安装 faiss。请安装 faiss-cpu 或使用兜底索引重建。")
        return faiss.read_index(str(faiss_path)), True

    if npy_path.exists():
        return np.load(npy_path).astype("float32"), False

    raise FileNotFoundError(f"未找到索引文件：{faiss_path} 或 {npy_path}")
