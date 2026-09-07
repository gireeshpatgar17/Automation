"""
Resume text extraction utilities for PDF and DOCX formats.
"""

import os
from pypdf import PdfReader
from docx import Document


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract raw text from a PDF file.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Extracted text as a string.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PDF file not found: {file_path}")
    
    text = []
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    except Exception as e:
        raise RuntimeError(f"Error reading PDF file {file_path}: {e}")
    
    return "\n".join(text)


def extract_text_from_docx(file_path: str) -> str:
    """
    Extract raw text from a DOCX file.

    Args:
        file_path: Path to the DOCX file.

    Returns:
        Extracted text as a string.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"DOCX file not found: {file_path}")
    
    try:
        doc = Document(file_path)
        text = [paragraph.text for paragraph in doc.paragraphs if paragraph.text]
    except Exception as e:
        raise RuntimeError(f"Error reading DOCX file {file_path}: {e}")
    
    return "\n".join(text)


def extract_text(file_path: str) -> str:
    """
    Extract raw text from a resume file (PDF or DOCX) based on extension.

    Args:
        file_path: Path to the resume file.

    Returns:
        Extracted text as a string.
    """
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}. Supported formats: .pdf, .docx")
