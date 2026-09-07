"""
Tests for text cleaning and preprocessing module.
"""

import pytest
from resume_matcher.preprocessor import clean_text, normalize_for_matching


def test_clean_text_empty():
    assert clean_text("") == ""
    assert clean_text(None) == ""


def test_clean_text_whitespace():
    raw = "   Hello   World!   \n\n\n   This is a   test.   \t"
    cleaned = clean_text(raw)
    assert cleaned == "Hello World!\nThis is a test."


def test_normalize_for_matching():
    raw = "  Python Developer with 5+ Years Experience! \n"
    normalized = normalize_for_matching(raw)
    assert normalized == "python developer with 5+ years experience!"
