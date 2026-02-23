"""
Unit-Tests für app/auth/utils.py

Diese Tests prüfen reine Funktionen ohne Datenbank oder HTTP 
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

def test_passwort_wird_nicht_als_klartext_gespeichert():
    """Der Hash darf niemals dem Originalpasswort gleichen."""
    hashed = hash_password("geheimesPasswort")
    assert hashed != "geheimesPasswort"


def test_hash_ist_nicht_leer():
    hashed = hash_password("test")
    assert len(hashed) > 10


def test_gleiches_passwort_ergibt_verschiedene_hashes():
    """bcrypt erzeugt immer einen anderen Salt → zwei Hashes sind nie gleich."""
    h1 = hash_password("passwort")
    h2 = hash_password("passwort")
    assert h1 != h2


def test_richtiges_passwort_wird_akzeptiert():
    hashed = hash_password("meinPasswort123")
    assert verify_password("meinPasswort123", hashed) is True


def test_falsches_passwort_wird_abgelehnt():
    hashed = hash_password("meinPasswort123")
    assert verify_password("falschesPasswort", hashed) is False


def test_leeres_passwort_wird_korrekt_behandelt():
    hashed = hash_password("")
    assert verify_password("", hashed) is True
    assert verify_password("nichtleer", hashed) is False


# ---------------------------------------------------------------------------
# create_access_token
# ---------------------------------------------------------------------------

def test_token_ist_ein_string():
    token = create_access_token({"sub": "42"})
    assert isinstance(token, str)
    assert len(token) > 0


def test_token_enthaelt_user_id():
    """Die übergebene User-ID muss im dekodierten Token stehen."""
    token = create_access_token({"sub": "99"})
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert payload["sub"] == "99"


def test_token_enthaelt_ablaufzeit():
    """Jeder Token braucht ein 'exp'-Feld, sonst gilt er als ewig gültig."""
    token = create_access_token({"sub": "1"})
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert "exp" in payload


def test_verschiedene_user_ids_erzeugen_verschiedene_tokens():
    t1 = create_access_token({"sub": "1"})
    t2 = create_access_token({"sub": "2"})
    assert t1 != t2
