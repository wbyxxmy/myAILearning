from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple
import re


@dataclass(frozen=True)
class Chunk:
    chunk_id: int
    source_path: str
    title_path: List[str]
    text: str


_HEADER_RE = re.compile(r"^(#{1,6})\s+(.*)\s*$")


def _split_markdown_sections(text: str) -> List[Tuple[List[str], str]]:
    """
    Return list of (title_path, section_text).
    Very small parser:
    - Recognizes #..###### headings
    - Accumulates content under the latest heading
    """
    lines = text.splitlines()
    sections: List[Tuple[List[str], List[str]]] = []
    title_stack: List[Tuple[int, str]] = []
    current_title_path: List[str] = ["(无标题)"]
    current_buf: List[str] = []

    def flush():
        nonlocal current_buf
        if current_buf:
            sections.append((current_title_path.copy(), current_buf))
            current_buf = []

    for line in lines:
        m = _HEADER_RE.match(line)
        if m:
            flush()
            level = len(m.group(1))
            title = m.group(2).strip()

            # Maintain stack
            while title_stack and title_stack[-1][0] >= level:
                title_stack.pop()
            title_stack.append((level, title))

            current_title_path = [t for _, t in title_stack]
        else:
            current_buf.append(line)

    flush()
    return [(tp, "\n".join(buf).strip()) for tp, buf in sections if "\n".join(buf).strip()]


def _split_by_length(s: str, target_chars: int, overlap_chars: int) -> List[str]:
    s = s.strip()
    if not s:
        return []
    if len(s) <= target_chars:
        return [s]

    chunks = []
    start = 0
    while start < len(s):
        end = min(len(s), start + target_chars)
        chunk = s[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= len(s):
            break
        start = max(0, end - overlap_chars)
    return chunks


def chunk_markdown(
    *,
    source_path: str,
    text: str,
    target_chars: int = 1200,
    overlap_chars: int = 150,
) -> List[Chunk]:
    sections = _split_markdown_sections(text)
    out: List[Chunk] = []
    chunk_id = 0
    for title_path, section_text in sections:
        parts = _split_by_length(section_text, target_chars, overlap_chars)
        for part in parts:
            out.append(
                Chunk(
                    chunk_id=chunk_id,
                    source_path=source_path,
                    title_path=title_path,
                    text=part,
                )
            )
            chunk_id += 1
    return out
