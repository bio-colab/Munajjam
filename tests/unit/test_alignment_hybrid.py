"""Focused tests for hybrid alignment strategy."""

from munajjam.core import Aligner


def test_hybrid_populates_stats(sample_segments, sample_ayahs):
    """Hybrid aligner should expose stats from the last run."""
    aligner = Aligner("dummy.wav", strategy="hybrid", energy_snap=False)
    results = aligner.align(sample_segments, sample_ayahs)

    assert results
    assert aligner.last_stats is not None
    assert aligner.last_stats.total_ayahs == len(sample_ayahs)
