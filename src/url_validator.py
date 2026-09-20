import re
from urllib.parse import urlparse


def is_valid_url(url):
    """Return True if the URL has a valid HTTP or HTTPS scheme."""
    if not isinstance(url, str):
        raise TypeError("url must be a string")

    parsed = urlparse(url)

    return (
        parsed.scheme in ("http", "https")
        and bool(parsed.netloc)
    )


def has_valid_domain(url):
    """Return True if the URL contains a domain with a dot."""
    if not isinstance(url, str):
        raise TypeError("url must be a string")

    parsed = urlparse(url)

    return bool(parsed.netloc) and "." in parsed.netloc


def normalize_url(url):
    """Remove surrounding whitespace and trailing slash."""
    if not isinstance(url, str):
        raise TypeError("url must be a string")

    return url.strip().rstrip("/")


def create_short_code(url):
    """Create a short code from the first three characters of the domain."""
    if not is_valid_url(url):
        raise ValueError("url is not valid")

    domain = urlparse(url).netloc
    return domain[:3].lower()
