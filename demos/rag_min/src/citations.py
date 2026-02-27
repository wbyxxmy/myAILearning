from __future__ import annotations

from typing import Dict, Any


def format_ref(chunk: Dict[str, Any]) -> str:
    # chunk_id -> "chunk-3" style
    return f"[{chunk['source_path']}#chunk-{chunk['chunk_id']}]"


def format_hit(rank: int, score: float, chunk: Dict[str, Any]) -> str:
    title = " / ".join(chunk.get("title_path") or [])
    return f"{rank:02d}. score={score:.4f} {format_ref(chunk)} title={title}"
