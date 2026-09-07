"""
Text cleaning and preprocessing utilities for resumes and job descriptions.
"""

import re


def clean_text(text: str) -> str:
    """
    Clean and normalize raw text by removing excessive whitespace, 
    special characters/noise, and standardizing line breaks.

    Args:
        text: Raw input text string.

    Returns:
        Cleaned and normalized text string.
    """
    if not text:
        return ""

    # Replace multiple newlines with single newline
    text = re.sub(r'\n\s*\n', '\n', text)
    
    # Replace tabs and carriage returns with spaces
    text = text.replace('\r', ' ').replace('\t', ' ')
    
    # Collapse multiple spaces into a single space within lines
    lines = [re.sub(r' +', ' ', line).strip() for line in text.split('\n')]
    
    # Filter out empty lines if needed, or keep structure
    text = '\n'.join([line for line in lines if line])

    return text


def normalize_for_matching(text: str) -> str:
    """
    Normalize text for keyword or term matching (lowercase, strip punctuation).

    Args:
        text: Input text string.

    Returns:
        Normalized lowercased text string.
    """
    if not text:
        return ""

    cleaned = clean_text(text)
    # Lowercase
    normalized = cleaned.lower()
    return normalized
