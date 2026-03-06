"""Validate dataset metadata and ground-truth timestamp continuity.

Usage:
    python dataset/validate.py
"""

from __future__ import annotations

import json
from pathlib import Path


def validate_ground_truth(path: Path) -> list[str]:
    errors: list[str] = []
    data = json.loads(path.read_text())

    ayahs = data.get("ayahs", [])
    if not ayahs:
        errors.append(f"{path}: no ayahs")
        return errors

    last_end = -1.0
    last_num = 0
    for idx, ayah in enumerate(ayahs):
        num = ayah.get("ayah_number")
        start = ayah.get("start")
        end = ayah.get("end")

        if not isinstance(num, int) or num <= 0:
            errors.append(f"{path}: invalid ayah_number at index {idx}")
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            errors.append(f"{path}: non-numeric start/end at index {idx}")
            continue
        if start < 0 or end <= start:
            errors.append(f"{path}: invalid time range at index {idx}")
        if start < last_end:
            errors.append(f"{path}: non-monotonic timestamp at index {idx}")
        if num <= last_num:
            errors.append(f"{path}: non-increasing ayah_number at index {idx}")

        last_end = end
        last_num = num

    return errors


def main() -> None:
    root = Path(__file__).parent
    metadata_path = root / "metadata.json"
    gt_dir = root / "ground_truth"

    errors: list[str] = []

    if not metadata_path.exists():
        errors.append("dataset/metadata.json missing")
    else:
        json.loads(metadata_path.read_text())

    if not gt_dir.exists():
        errors.append("dataset/ground_truth directory missing")
    else:
        gt_files = sorted(gt_dir.glob("*.json"))
        if not gt_files:
            errors.append("dataset/ground_truth has no JSON files")
        for gt_file in gt_files:
            errors.extend(validate_ground_truth(gt_file))

    if errors:
        print("dataset validation FAILED")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("dataset validation PASSED")


if __name__ == "__main__":
    main()
