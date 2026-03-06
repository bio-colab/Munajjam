"""Integration test for the full alignment pipeline on Surah Al-Fatiha fixtures."""

from munajjam.core import Aligner


def test_full_pipeline_fatiha_fixture(sample_segments, sample_ayahs, sample_silences):
    """Runs auto strategy with post-processing enabled on fixture data."""
    aligner = Aligner("dummy.wav", strategy="auto", energy_snap=False)
    results = aligner.align(sample_segments, sample_ayahs, silences_ms=sample_silences)

    assert len(results) >= 3
    assert all(result.ayah.surah_id == 1 for result in results)
    assert all(result.end_time > result.start_time for result in results)
