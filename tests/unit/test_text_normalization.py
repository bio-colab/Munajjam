"""Unit tests for extended Arabic normalization edge cases."""

import pytest

from munajjam.core.arabic import normalize_arabic


@pytest.mark.parametrize(
    "raw_text,expected",
    [
        ("إِنَّ شَانِئَكَ هُوَ الْأَبْتَرُ", "ان شانيك هو الابتر"),
        ("هدى", "هدي"),
        ("رحمة", "رحمه"),
        ("سُئِلَ", "سيل"),
        ("شيءٌ", "شيء"),
        ("   بِسْمِ،  اللَّهِ! ", "بسم الله"),
    ],
)
def test_normalize_arabic_edge_cases(raw_text, expected):
    """Normalization should unify known Arabic orthographic variants."""
    assert normalize_arabic(raw_text) == expected


def test_normalize_arabic_preserves_word_boundaries_with_tashkeel():
    """Normalization must keep token boundaries stable for alignment."""
    original = "ٱلْحَمْدُ لِلَّٰهِ رَبِّ ٱلْعَٰلَمِينَ"
    normalized = normalize_arabic(original)

    assert len(normalized.split()) == len(original.split())
