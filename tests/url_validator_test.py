import pytest
from src.url_validator import (
    is_valid_url,
    has_valid_domain,
    normalize_url,
    create_short_code,
)


def test_valid_url():
    """Test a valid HTTPS URL."""
    url = "https://example.com"

    result = is_valid_url(url)

    assert result == True


def test_invalid_url():
    """Test an invalid URL."""
    url = "example.com"

    result = is_valid_url(url)

    assert result == False


def test_url_type_error():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_url(12345)


def test_create_short_code():
    """Test short code generation."""
    url = "https://google.com"

    result = create_short_code(url)

    assert result == "goo"
