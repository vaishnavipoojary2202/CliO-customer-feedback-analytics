"""Utilities for inspecting Amazon Reviews 2023 JSONL.GZ files.

Records are streamed rather than loaded all at once. The smartphone title
filter is heuristic and needs manual quality checks before final analysis.
"""
from __future__ import annotations

import gzip
import json
import re
from pathlib import Path
from typing import Any, Iterator

PHONE_PATTERN = re.compile(
    r"\\b(?:iphone|smartphone|smart phone|cell phone|mobile phone|"
    r"google pixel|pixel\\s+\\d|galaxy\\s+[sazm]\\d|galaxy note|"
    r"galaxy fold|galaxy flip|oneplus|redmi|poco phone|xiaomi phone|"
    r"motorola edge|moto g\\d|moto edge|sony xperia|nokia [gxc]\\d|"
    r"asus zenfone|nothing phone|oppo find|oppo reno|vivo [xv]\\d|"
    r"realme \\d|huawei p\\d|huawei mate|honor magic)\\b",
    re.IGNORECASE,
)
ACCESSORY_PATTERN = re.compile(
    r"\\b(?:phone case|protective case|phone cover|screen protector|"
    r"tempered glass|charger|charging cable|usb cable|adapter|"
    r"power bank|phone mount|phone holder|phone stand|"
    r"replacement battery|camera lens protector|phone skin|earbuds|"
    r"headphones|stylus)\\b",
    re.IGNORECASE,
)


def iter_jsonl_gz(path: str | Path) -> Iterator[dict[str, Any]]:
    """Yield valid JSON objects from a compressed JSON Lines file."""
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"Dataset file not found: {file_path}")
    with gzip.open(file_path, "rt", encoding="utf-8") as stream:
        for line in stream:
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(record, dict):
                yield record


def is_candidate_smartphone(title: str | None) -> bool:
    """Heuristic candidate filter. Manually inspect results before use."""
    normalized = (title or "").strip()
    return bool(normalized and PHONE_PATTERN.search(normalized)
                and not ACCESSORY_PATTERN.search(normalized))


def inspect_jsonl_gz(path: str | Path, limit: int = 3) -> list[dict[str, Any]]:
    """Return a short preview of a compressed JSONL file."""
    if limit < 1:
        raise ValueError("limit must be >= 1")
    preview: list[dict[str, Any]] = []
    for record in iter_jsonl_gz(path):
        preview.append(record)
        if len(preview) >= limit:
            break
    return preview


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    raw_dir = root / "data" / "raw"
    print(f"Place the downloaded .jsonl.gz files in: {raw_dir}")
    print("Inspect each file schema before processing the complete dataset.")
