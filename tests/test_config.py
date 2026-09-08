import pytest
from resume_matcher.config import Config, get_config

def test_default_config():
    config = get_config()
    assert isinstance(config, Config)
    assert config.spacy_model == "en_core_web_sm"
    assert config.max_file_size_mb == 10
    assert config.similarity_threshold == 0.5
