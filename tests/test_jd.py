"""
Tests for job description acceptance, cleaning, and validation.
"""

import pytest
from resume_matcher.jd import JobDescription


def test_job_description_valid():
    text = """
    Senior Python Engineer
    We are looking for a Senior Python Engineer with experience in Django, PostgreSQL, and AWS.
    Responsibilities include designing scalable microservices and mentoring junior developers.
    """
    jd = JobDescription(raw_text=text, title="Senior Python Engineer", company="TechCorp")
    assert jd.validate() is True
    assert jd.title == "Senior Python Engineer"
    assert jd.company == "TechCorp"
    assert "senior python engineer" in jd.normalized_text
    assert len(jd.cleaned_text.split()) > 10


def test_job_description_empty():
    jd = JobDescription(raw_text="")
    assert jd.validate() is False

    jd_whitespace = JobDescription(raw_text="   \n\t  ")
    assert jd_whitespace.validate() is False


def test_job_description_too_short():
    jd = JobDescription(raw_text="Python job")
    assert jd.validate() is False


def test_job_description_none():
    jd = JobDescription(raw_text=None)
    assert jd.validate() is False
    assert jd.cleaned_text == ""
