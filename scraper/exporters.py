from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Iterable

from .core import Quote


def export_csv(quotes: Iterable[Quote], output_path: str | Path) -> None:
    path = Path(output_path)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["text", "author", "tags"])
        for quote in quotes:
            writer.writerow([quote.text, quote.author, ";".join(quote.tags)])


def export_json(quotes: Iterable[Quote], output_path: str | Path) -> None:
    path = Path(output_path)
    payload = [
        {"text": q.text, "author": q.author, "tags": q.tags} for q in quotes
    ]
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
