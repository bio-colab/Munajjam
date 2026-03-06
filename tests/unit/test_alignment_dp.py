"""Focused tests for DP alignment strategy."""

import json
from pathlib import Path

from munajjam.core import Aligner


EXPECTED_PATH = Path("tests/fixtures/expected_outputs/fatiha_fixture_alignment.json")


def test_dp_strategy_matches_expected_fixture_alignment(sample_segments, sample_ayahs):
    """DP alignment should match deterministic fixture output."""
    expected = json.loads(EXPECTED_PATH.read_text())["expected"]

    aligner = Aligner("dummy.wav", strategy="dp", energy_snap=False)
    results = aligner.align(sample_segments, sample_ayahs)

    assert [r.ayah.ayah_number for r in results] == expected["ayah_numbers"]
    assert [round(r.start_time, 1) for r in results] == expected["start_times"]
    assert [round(r.end_time, 1) for r in results] == expected["end_times"]
    assert all(0.0 <= r.similarity_score <= 1.0 for r in results)
