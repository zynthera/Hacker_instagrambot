import pytest
from message_generator import generate_group_message
from rate_limiter import RateLimiter

def test_message_generator():
    message = generate_group_message("testuser", "fake_api_key")
    assert "@" in message

def test_rate_limiter():
    limiter = RateLimiter(rate_limit=2, time_window=5)
    assert limiter.is_allowed()
    assert limiter.is_allowed()
    assert not limiter.is_allowed()