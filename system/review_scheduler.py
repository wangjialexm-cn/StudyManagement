#!/usr/bin/env python3
"""
C+错题复现调度器

固定用法：
    python3 system/review_scheduler.py --day 5

数据约定：
    mistakes/day4.json
    mistakes/day5.json
    mistakes/day6.json

复现规则：
    D+1、D+3、D+7

输出：
    review/daily_review.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


REVIEW_INTERVALS = {
    1: "D+1",
    3: "D+3",
    7: "D+7",
}


SUBJECTS = ("math", "physics", "chemistry", "english")


def project_root() -> Path:
    """Return the project root based on this script location."""
    return Path(__file__).resolve().parents[1]


def extract_day_from_filename(path: Path) -> Optional[int]:
    """Extract day number from filenames like day4.json."""
    match = re.fullmatch(r"day(\d+)\.json", path.name, flags=re.IGNORECASE)
    if not match:
        return None
    return int(match.group(1))


def load_json(path: Path) -> Optional[Dict[str, Any]]:
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Skip invalid file: {path} ({exc})")
        return None

    if not isinstance(data, dict):
        print(f"Skip non-object JSON file: {path}")
        return None
    return data


def iter_mistake_files(mistake_dir: Path) -> Iterable[Tuple[int, Path]]:
    """Yield (day, path) for files named dayN.json, sorted by day."""
    if not mistake_dir.exists():
        return []

    files: List[Tuple[int, Path]] = []
    for path in mistake_dir.glob("day*.json"):
        day = extract_day_from_filename(path)
        if day is not None:
            files.append((day, path))
    return sorted(files, key=lambda item: item[0])


def normalize_mistakes(data: Dict[str, Any], file_day: int) -> List[Dict[str, Any]]:
    """
    Support the required C+ JSON structure:

    {
      "day": 4,
      "mistakes": {
        "math": [],
        "physics": [],
        "chemistry": [],
        "english": []
      }
    }

    Also tolerates a legacy shape where "mistakes" is a list, or a single
    mistake object with subject/question fields.
    """
    normalized: List[Dict[str, Any]] = []
    mistakes = data.get("mistakes", {})

    if isinstance(mistakes, dict):
        for subject in SUBJECTS:
            subject_items = mistakes.get(subject, [])
            if not isinstance(subject_items, list):
                continue
            for index, item in enumerate(subject_items, start=1):
                if isinstance(item, dict):
                    normalized.append({
                        **item,
                        "subject": subject,
                        "mistake_day": file_day,
                        "source_index": index,
                    })
        return normalized

    if isinstance(mistakes, list):
        for index, item in enumerate(mistakes, start=1):
            if isinstance(item, dict):
                normalized.append({
                    **item,
                    "subject": item.get("subject", "unknown"),
                    "mistake_day": file_day,
                    "source_index": index,
                })
        return normalized

    if any(key in data for key in ("subject", "question", "knowledge_point")):
        normalized.append({
            **data,
            "subject": data.get("subject", "unknown"),
            "mistake_day": file_day,
            "source_index": 1,
        })

    return normalized


def should_review(mistake_day: int, current_day: int) -> Tuple[bool, Optional[str]]:
    diff = current_day - mistake_day
    interval = REVIEW_INTERVALS.get(diff)
    return interval is not None, interval


def build_review_item(item: Dict[str, Any], current_day: int, interval: str, source_file: Path) -> Dict[str, Any]:
    mistake_day = int(item["mistake_day"])
    return {
        "subject": item.get("subject", "unknown"),
        "question": item.get("question", ""),
        "review_interval": interval,
        "mistake_day": mistake_day,
        "current_day": current_day,
        "days_after_mistake": current_day - mistake_day,
        "knowledge_point": item.get("knowledge_point", ""),
        "error_type": item.get("error_type", ""),
        "student_answer": item.get("student_answer", ""),
        "correct_answer": item.get("correct_answer", ""),
        "source_file": str(source_file.as_posix()),
        "source_index": item.get("source_index"),
    }


def generate_review_plan(current_day: int, root: Optional[Path] = None) -> Dict[str, Any]:
    root = root or project_root()
    mistake_dir = root / "mistakes"
    review_dir = root / "review"
    output_path = review_dir / "daily_review.json"

    review_items: List[Dict[str, Any]] = []
    scanned_files: List[str] = []

    for mistake_day, path in iter_mistake_files(mistake_dir):
        scanned_files.append(str(path.relative_to(root)))
        data = load_json(path)
        if data is None:
            continue

        need_review, interval = should_review(mistake_day, current_day)
        if not need_review or interval is None:
            continue

        for item in normalize_mistakes(data, mistake_day):
            review_items.append(build_review_item(item, current_day, interval, path.relative_to(root)))

    result = {
        "day": current_day,
        "review_rules": ["D+1", "D+3", "D+7"],
        "source_dir": str(mistake_dir.relative_to(root)),
        "scanned_files": scanned_files,
        "review_count": len(review_items),
        "review_items": review_items,
    }

    review_dir.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")

    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate daily C+ review items from mistakes/dayN.json files.")
    parser.add_argument("--day", type=int, required=True, help="Current day number, for example: --day 5")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = generate_review_plan(args.day)
    print(f"Review generated: {result['review_count']} items for day {result['day']}")


if __name__ == "__main__":
    main()
