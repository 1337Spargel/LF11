"""
Unit tests for app/auth/utils.py

These tests check pure functions without a database or HTTP.
"""
from jose import jwt

from app.auth.utils import (
    hash_password,
    verify_password,
    create_access_token,
    SECRET_KEY,
    ALGORITHM,
)


# ---------------------------------------------------------------------------
# hash_password & verify_password
# ---------------------------------------------------------------------------

def test_password_is_not_stored_as_plaintext():
    """The hash must never equal the original password."""
    hashed = hash_password("secretPassword")
    assert hashed != "secretPassword"


def test_hash_is_not_empty():
    hashed = hash_password("test")
    assert len(hashed) > 10


def test_same_password_produces_different_hashes():
    """bcrypt always generates a different salt → two hashes are never equal."""
    h1 = hash_password("password")
    h2 = hash_password("password")
    assert h1 != h2


def test_correct_password_is_accepted():
    hashed = hash_password("myPassword123")
    assert verify_password("myPassword123", hashed) is True


def test_wrong_password_is_rejected():
    hashed = hash_password("myPassword123")
    assert verify_password("wrongPassword", hashed) is False


def test_empty_password_is_handled_correctly():
    hashed = hash_password("")
    assert verify_password("", hashed) is True
    assert verify_password("notEmpty", hashed) is False


# ---------------------------------------------------------------------------
# create_access_token
# ---------------------------------------------------------------------------

def test_token_is_a_string():
    token = create_access_token({"sub": "42"})
    assert isinstance(token, str)
    assert len(token) > 0


def test_token_contains_user_id():
    """The provided user ID must be present in the decoded token."""
    token = create_access_token({"sub": "99"})
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert payload["sub"] == "99"


def test_token_contains_expiry():
    """Every token needs an 'exp' field, otherwise it is considered eternal."""
    token = create_access_token({"sub": "1"})
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert "exp" in payload


def test_different_user_ids_produce_different_tokens():
    t1 = create_access_token({"sub": "1"})
    t2 = create_access_token({"sub": "2"})
    assert t1 != t2
