"""Focused tests for greedy alignment strategy."""

from munajjam.core import Aligner


def test_greedy_strategy_returns_monotonic_timestamps(sample_segments, sample_ayahs):
    """Greedy aligner should keep strictly increasing non-overlapping ranges."""
    aligner = Aligner("dummy.wav", strategy="greedy", energy_snap=False)
    results = aligner.align(sample_segments, sample_ayahs)

    assert results
    assert all(r.end_time > r.start_time for r in results)
    assert all(results[i].start_time <= results[i + 1].start_time for i in range(len(results) - 1))
