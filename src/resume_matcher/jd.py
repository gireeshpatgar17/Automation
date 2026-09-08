"""
Job description acceptance, cleaning, and validation module.
"""

from resume_matcher.preprocessor import clean_text, normalize_for_matching


class JobDescription:
    """
    Represents a job description with raw text, cleaned text, and validation checks.
    """

    def __init__(self, raw_text: str, title: str = "", company: str = ""):
        self.raw_text = raw_text if raw_text else ""
        self.title = title
        self.company = company
        self.cleaned_text = clean_text(self.raw_text)
        self.normalized_text = normalize_for_matching(self.raw_text)

    def validate(self) -> bool:
        """
        Validate that the job description contains meaningful content.

        Returns:
            True if valid, False otherwise.
        """
        if not self.raw_text or not self.raw_text.strip():
            return False
        # Minimum threshold of words or characters for a valid job description
        if len(self.cleaned_text.split()) < 3:
            return False
        return True

    def __repr__(self) -> str:
        return f"<JobDescription title='{self.title}' company='{self.company}' words={len(self.cleaned_text.split())}>"
