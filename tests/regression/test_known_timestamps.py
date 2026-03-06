"""Regression tests for fixture-based timestamp expectations."""

import json
from pathlib import Path

from munajjam.core import Aligner


EXPECTED_PATH = Path("tests/fixtures/expected_outputs/fatiha_fixture_alignment.json")


def test_known_timestamps_stable_for_fixture_data(sample_segments, sample_ayahs):
    """Guard against regressions in fixture starts/ends and ayah mapping."""
    expected = json.loads(EXPECTED_PATH.read_text())["expected"]

    aligner = Aligner("dummy.wav", strategy="greedy", energy_snap=False, fix_drift=False)
    results = aligner.align(sample_segments, sample_ayahs)

    assert [r.ayah.ayah_number for r in results] == expected["ayah_numbers"]
    assert [round(r.start_time, 1) for r in results] == expected["start_times"]
    assert [round(r.end_time, 1) for r in results] == expected["end_times"]
