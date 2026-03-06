"""Focused tests for DP alignment strategy."""

from munajjam.core import Aligner


def test_dp_strategy_returns_one_result_per_ayah(sample_segments, sample_ayahs):
    """DP alignment should produce an output row for each reference ayah."""
    aligner = Aligner("dummy.wav", strategy="dp", energy_snap=False)
    results = aligner.align(sample_segments, sample_ayahs)

    assert len(results) >= 3
    assert all(0.0 <= r.similarity_score <= 1.0 for r in results)
