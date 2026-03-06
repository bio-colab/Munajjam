"""Runnable benchmark for fixture-based alignment quality checks.

Usage:
    PYTHONPATH=munajjam python benchmarks/run.py --output benchmarks/results/latest.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from statistics import mean

from munajjam.core import Aligner
from munajjam.models import Ayah, Segment, SegmentType


def fixture_segments() -> list[Segment]:
    return [
        Segment(
            id=0,
            surah_id=1,
            start=0.0,
            end=4.5,
            text="أَعُوذُ بِاللَّهِ مِنَ الشَّيْطَانِ الرَّجِيمِ",
            type=SegmentType.ISTIADHA,
        ),
        Segment(
            id=1,
            surah_id=1,
            start=5.0,
            end=8.5,
            text="بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ",
            type=SegmentType.BASMALA,
        ),
        Segment(
            id=2,
            surah_id=1,
            start=9.0,
            end=13.5,
            text="الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ",
            type=SegmentType.AYAH,
        ),
        Segment(
            id=3,
            surah_id=1,
            start=14.0,
            end=18.0,
            text="الرَّحْمَٰنِ الرَّحِيمِ",
            type=SegmentType.AYAH,
        ),
    ]


def fixture_ayahs() -> list[Ayah]:
    return [
        Ayah(id=1, surah_id=1, ayah_number=1, text="بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"),
        Ayah(id=2, surah_id=1, ayah_number=2, text="الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ"),
        Ayah(id=3, surah_id=1, ayah_number=3, text="الرَّحْمَٰنِ الرَّحِيمِ"),
        Ayah(id=4, surah_id=1, ayah_number=4, text="مَالِكِ يَوْمِ الدِّينِ"),
    ]


def evaluate_strategy(strategy: str) -> dict:
    expected_starts = {1: 5.0, 2: 9.0, 3: 14.0}
    expected_set = set(expected_starts)

    aligner = Aligner("dummy.wav", strategy=strategy, energy_snap=False, fix_drift=False)
    results = aligner.align(fixture_segments(), fixture_ayahs())

    pred_starts = {r.ayah.ayah_number: r.start_time for r in results}
    matched = expected_set.intersection(pred_starts)

    mae = mean(abs(pred_starts[a] - expected_starts[a]) for a in matched) if matched else None
    ayah_accuracy = len(matched) / len(expected_set)

    return {
        "strategy": strategy,
        "predicted_ayah_numbers": sorted(pred_starts),
        "matched_ayahs": len(matched),
        "total_reference_ayahs": len(expected_set),
        "ayah_accuracy": round(ayah_accuracy, 4),
        "mae_start_seconds": None if mae is None else round(mae, 4),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="benchmarks/results/latest.json")
    args = parser.parse_args()

    payload = {
        "benchmark": "fixture_alignment",
        "strategies": [evaluate_strategy(s) for s in ("auto", "hybrid", "dp", "greedy")],
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    print(f"wrote benchmark results to {output_path}")


if __name__ == "__main__":
    main()
