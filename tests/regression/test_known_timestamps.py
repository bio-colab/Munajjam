"""Regression tests for fixture-based timestamp expectations."""

from munajjam.core import Aligner


def test_known_timestamps_stable_for_fixture_data(sample_segments, sample_ayahs):
    """Guard against large regressions in start times for fixture alignment."""
    aligner = Aligner("dummy.wav", strategy="greedy", energy_snap=False, fix_drift=False)
    results = aligner.align(sample_segments, sample_ayahs)

    starts = [round(r.start_time, 1) for r in results]
    assert starts == [5.0, 9.0, 14.0]
