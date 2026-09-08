import os
from dataclasses import dataclass

@dataclass
class Config:
    """Application configuration settings."""
    spacy_model: str = os.getenv("RESUME_MATCHER_SPACY_MODEL", "en_core_web_sm")
    max_file_size_mb: int = int(os.getenv("RESUME_MATCHER_MAX_FILE_SIZE_MB", "10"))
    similarity_threshold: float = float(os.getenv("RESUME_MATCHER_SIMILARITY_THRESHOLD", "0.5"))

def get_config() -> Config:
    """Get application configuration instance."""
    return Config()
