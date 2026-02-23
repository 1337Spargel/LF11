"""
Integrationstests für den /api/bookings-Endpoint.

Diese Tests nutzen 'client' und 'db' aus conftest.py.
Jeder Test bekommt eine leere In-Memory-Datenbank und legt
seine eigenen Testdaten an.
"""
import pytest

from app.auth.utils import hash_password
from app.models.building import Building
from app.models.floor import Floor
from app.models.room import Room
from app.models.seat import Seat
from app.models.user import User


@pytest.fixture()
def test_data(db):
    """
    Legt die minimale Datenmenge an, die für Buchungstests nötig ist:
    1 User → 1 Gebäude → 1 Etage → 1 Raum → 1 Sitzplatz
    """
    user = User(
        name="Test User",
        email="test@test.de",
        hashed_password=hash_password("test123"),
    )
    building = Building(name="Testgebäude")
    db.add_all([user, building])
    db.flush()

    floor = Floor(building_id=building.id, name="Erdgeschoss", floor_number=0)
    db.add(floor)
    db.flush()

    room = Room(floor_id=floor.id, name="Raum 1", room_number="1", capacity=1)
    db.add(room)
    db.flush()

    seat = Seat(room_id=room.id, seat_number="1")
    db.add(seat)
    db.commit()
    db.refresh(seat)
    db.refresh(user)

    return {"user_id": user.id, "seat_id": seat.id}


# ---------------------------------------------------------------------------
# Erfolgreiche Buchung
# ---------------------------------------------------------------------------

def test_buchung_erstellen_gibt_201(client, test_data):
    """Eine valide Buchung muss mit 201 Created beantwortet werden."""
    res = client.post("/api/bookings/", json={
        "seat_id": test_data["seat_id"],
        "user_id": test_data["user_id"],
        "date": "2025-06-01",
    })
    assert res.status_code == 201


def test_buchung_enthaelt_korrekte_daten(client, test_data):
    """Die Antwort muss seat_id und das gebuchte Datum enthalten."""
    res = client.post("/api/bookings/", json={
        "seat_id": test_data["seat_id"],
        "user_id": test_data["user_id"],
        "date": "2025-06-01",
    })
    body = res.json()
    assert body["seat_id"] == test_data["seat_id"]
    assert body["date"] == "2025-06-01"
    assert "id" in body


# ---------------------------------------------------------------------------
# Doppelbuchung (kritischste Business-Logik)
# ---------------------------------------------------------------------------

def test_doppelbuchung_selber_sitz_selber_tag_gibt_409(client, test_data):
    """Zweite Buchung desselben Sitzes am selben Tag muss mit 409 abgelehnt werden."""
    payload = {
        "seat_id": test_data["seat_id"],
        "user_id": test_data["user_id"],
        "date": "2025-06-10",
    }
    res1 = client.post("/api/bookings/", json=payload)
    assert res1.status_code == 201  # erste Buchung klappt

    res2 = client.post("/api/bookings/", json=payload)
    assert res2.status_code == 409  # zweite Buchung wird abgelehnt


def test_gleicher_sitz_anderer_tag_ist_erlaubt(client, test_data):
    """Derselbe Sitz darf an verschiedenen Tagen gebucht werden."""
    client.post("/api/bookings/", json={
        "seat_id": test_data["seat_id"],
        "user_id": test_data["user_id"],
        "date": "2025-06-11",
    })
    res = client.post("/api/bookings/", json={
        "seat_id": test_data["seat_id"],
        "user_id": test_data["user_id"],
        "date": "2025-06-12",  # anderer Tag
    })
    assert res.status_code == 201


# ---------------------------------------------------------------------------
# Fehlerfall: unbekannter Sitzplatz
# ---------------------------------------------------------------------------

def test_buchung_fuer_unbekannten_sitz_gibt_404(client, test_data):
    """Eine Buchung für eine nicht existierende seat_id muss 404 zurückgeben."""
    res = client.post("/api/bookings/", json={
        "seat_id": 99999,
        "user_id": test_data["user_id"],
        "date": "2025-06-15",
    })
    assert res.status_code == 404


# ---------------------------------------------------------------------------
# Buchung stornieren
# ---------------------------------------------------------------------------

def test_buchung_stornieren_gibt_204(client, test_data):
    """Eine bestehende Buchung erfolgreich löschen → 204 No Content."""
    res = client.post("/api/bookings/", json={
        "seat_id": test_data["seat_id"],
        "user_id": test_data["user_id"],
        "date": "2025-06-20",
    })
    booking_id = res.json()["id"]

    del_res = client.delete(f"/api/bookings/{booking_id}")
    assert del_res.status_code == 204


def test_nach_stornierung_wieder_buchbar(client, test_data):
    """Nach dem Stornieren darf der Sitz am selben Tag neu gebucht werden."""
    payload = {
        "seat_id": test_data["seat_id"],
        "user_id": test_data["user_id"],
        "date": "2025-06-21",
    }
    res1 = client.post("/api/bookings/", json=payload)
    booking_id = res1.json()["id"]

    client.delete(f"/api/bookings/{booking_id}")

    res2 = client.post("/api/bookings/", json=payload)
    assert res2.status_code == 201


def test_unbekannte_buchung_stornieren_gibt_404(client, test_data):
    """Stornieren einer nicht existierenden Buchung muss 404 zurückgeben."""
    res = client.delete("/api/bookings/99999")
    assert res.status_code == 404
