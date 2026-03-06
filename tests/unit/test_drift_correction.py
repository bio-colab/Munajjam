"""Tests for drift correction toggles inside Aligner."""

import json
from pathlib import Path

from munajjam.core import Aligner


EXPECTED_PATH = Path("tests/fixtures/expected_outputs/fatiha_fixture_alignment.json")


def test_drift_correction_can_be_disabled(sample_segments, sample_ayahs):
    """When fix_drift=False, alignment should still return deterministic fixture mapping."""
    expected = json.loads(EXPECTED_PATH.read_text())["expected"]

    aligner = Aligner(
        "dummy.wav",
        strategy="hybrid",
        fix_drift=False,
        fix_overlaps=False,
        energy_snap=False,
    )
    results = aligner.align(sample_segments, sample_ayahs)

    assert [r.ayah.ayah_number for r in results] == expected["ayah_numbers"]
    assert [round(r.start_time, 1) for r in results] == expected["start_times"]
