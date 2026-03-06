"""Integration test for sequential batch processing of multiple audio jobs."""

from munajjam.core import Aligner


def test_batch_processing_two_jobs(sample_segments, sample_ayahs):
    """A single Aligner instance should process multiple jobs deterministically."""
    aligner = Aligner("dummy.wav", strategy="hybrid", energy_snap=False)

    first = aligner.align(sample_segments, sample_ayahs)
    second = aligner.align(sample_segments, sample_ayahs)

    assert len(first) == len(second) >= 3
    assert [r.ayah.ayah_number for r in first] == [r.ayah.ayah_number for r in second]
