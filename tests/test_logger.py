import pytest
from resume_matcher.logger import get_logger

def test_get_logger():
    logger = get_logger("test_logger")
    assert logger is not None
    assert logger.name == "test_logger"
    assert logger.level == 20  # INFO level
