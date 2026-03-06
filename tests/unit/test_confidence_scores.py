"""Tests for confidence and derived metrics on alignment results."""

from munajjam.models import AlignmentResult, Ayah


def _ayah() -> Ayah:
    return Ayah(id=1, surah_id=1, ayah_number=1, text="بسم الله الرحمن الرحيم")


def test_is_high_confidence_true_at_threshold():
    result = AlignmentResult(
        ayah=_ayah(),
        start_time=0.0,
        end_time=3.2,
        transcribed_text="بسم الله الرحمن الرحيم",
        similarity_score=0.8,
    )

    assert result.is_high_confidence is True


def test_is_high_confidence_false_below_threshold():
    result = AlignmentResult(
        ayah=_ayah(),
        start_time=0.0,
        end_time=3.2,
        transcribed_text="بسم الله الرحمن الرحيم",
        similarity_score=0.79,
    )

    assert result.is_high_confidence is False
    assert result.duration == 3.2
