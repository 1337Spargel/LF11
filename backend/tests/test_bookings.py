"""
Integration tests for the /api/bookings endpoint.

These tests use 'client' and 'db' from conftest.py.
Each test gets an empty in-memory database and creates
its own test data.
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
    Creates the minimum data needed for booking tests:
    1 user → 1 building → 1 floor → 1 room → 1 seat
    """
    user = User(
        name="Test User",
        email="test@test.com",
        hashed_password=hash_password("test123"),
    )
    building = Building(name="Test Building")
    db.add_all([user, building])
    db.flush()

    floor = Floor(building_id=building.id, name="Ground Floor", floor_number=0)
    db.add(floor)
    db.flush()

    room = Room(floor_id=floor.id, name="Room 1", room_number="1", capacity=1)
    db.add(room)
    db.flush()

    seat = Seat(room_id=room.id, seat_number="1")
    db.add(seat)
    db.commit()
    db.refresh(seat)
    db.refresh(user)

    return {"user_id": user.id, "seat_id": seat.id}


# ---------------------------------------------------------------------------
# Successful booking
# ---------------------------------------------------------------------------

def test_create_booking_returns_201(client, test_data):
    """A valid booking must be answered with 201 Created."""
    res = client.post("/api/bookings/", json={
        "seat_id": test_data["seat_id"],
        "user_id": test_data["user_id"],
        "date": "2025-06-01",
    })
    assert res.status_code == 201


def test_booking_contains_correct_data(client, test_data):
    """The response must contain the seat_id and the booked date."""
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
# Double booking (most critical business logic)
# ---------------------------------------------------------------------------

def test_double_booking_same_seat_same_day_returns_409(client, test_data):
    """A second booking of the same seat on the same day must be rejected with 409."""
    payload = {
        "seat_id": test_data["seat_id"],
        "user_id": test_data["user_id"],
        "date": "2025-06-10",
    }
    res1 = client.post("/api/bookings/", json=payload)
    assert res1.status_code == 201  # first booking succeeds

    res2 = client.post("/api/bookings/", json=payload)
    assert res2.status_code == 409  # second booking is rejected


def test_same_seat_different_day_is_allowed(client, test_data):
    """The same seat may be booked on different days."""
    client.post("/api/bookings/", json={
        "seat_id": test_data["seat_id"],
        "user_id": test_data["user_id"],
        "date": "2025-06-11",
    })
    res = client.post("/api/bookings/", json={
        "seat_id": test_data["seat_id"],
        "user_id": test_data["user_id"],
        "date": "2025-06-12",  # different day
    })
    assert res.status_code == 201


# ---------------------------------------------------------------------------
# Error case: unknown seat
# ---------------------------------------------------------------------------

def test_booking_for_unknown_seat_returns_404(client, test_data):
    """A booking for a non-existent seat_id must return 404."""
    res = client.post("/api/bookings/", json={
        "seat_id": 99999,
        "user_id": test_data["user_id"],
        "date": "2025-06-15",
    })
    assert res.status_code == 404


# ---------------------------------------------------------------------------
# Cancel booking
# ---------------------------------------------------------------------------

def test_cancel_booking_returns_204(client, test_data):
    """Successfully deleting an existing booking → 204 No Content."""
    res = client.post("/api/bookings/", json={
        "seat_id": test_data["seat_id"],
        "user_id": test_data["user_id"],
        "date": "2025-06-20",
    })
    booking_id = res.json()["id"]

    del_res = client.delete(f"/api/bookings/{booking_id}")
    assert del_res.status_code == 204


def test_rebookable_after_cancellation(client, test_data):
    """After cancellation the seat can be booked again on the same day."""
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


def test_cancel_unknown_booking_returns_404(client, test_data):
    """Cancelling a non-existent booking must return 404."""
    res = client.delete("/api/bookings/99999")
    assert res.status_code == 404
