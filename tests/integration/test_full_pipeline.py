"""Integration test for the full alignment pipeline on Surah Al-Fatiha fixtures."""

import json
from pathlib import Path

from munajjam.core import Aligner


EXPECTED_PATH = Path("tests/fixtures/expected_outputs/fatiha_fixture_alignment.json")


def test_full_pipeline_fatiha_fixture(sample_segments, sample_ayahs, sample_silences):
    """Runs auto strategy with post-processing enabled on fixture data."""
    expected = json.loads(EXPECTED_PATH.read_text())["expected"]

    aligner = Aligner("dummy.wav", strategy="auto", energy_snap=False)
    results = aligner.align(sample_segments, sample_ayahs, silences_ms=sample_silences)

    assert [result.ayah.ayah_number for result in results] == expected["ayah_numbers"]
    assert [round(result.start_time, 1) for result in results] == expected["start_times"]
    assert [round(result.end_time, 1) for result in results] == [8.5, 13.0, 18.0]
    assert all(result.end_time > result.start_time for result in results)
