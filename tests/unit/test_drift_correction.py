"""Tests for drift correction toggles inside Aligner."""

from munajjam.core import Aligner


def test_drift_correction_can_be_disabled(sample_segments, sample_ayahs):
    """When fix_drift=False, alignment should still run and return valid results."""
    aligner = Aligner(
        "dummy.wav",
        strategy="hybrid",
        fix_drift=False,
        fix_overlaps=False,
        energy_snap=False,
    )
    results = aligner.align(sample_segments, sample_ayahs)

    assert results
    assert len(results) >= 3
