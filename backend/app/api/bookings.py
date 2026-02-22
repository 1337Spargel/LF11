from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from pydantic import BaseModel
from datetime import date

from app.db.db import get_db
from app.models.booking import Booking
from app.models.seat import Seat

router = APIRouter()

# --- Schemas ---
class BookingOut(BaseModel):
    id: int
    seat_id: int
    user_id: int
    date: date

    class Config:
        from_attributes = True

class BookingCreate(BaseModel):
    seat_id: int
    user_id: int
    date: date

# --- Endpunkte ---
@router.get("/", response_model=list[BookingOut])
def get_bookings(user_id: int | None = None, db: Session = Depends(get_db)):
    """Alle Buchungen, optional gefiltert nach Nutzer"""
    query = db.query(Booking)
    if user_id:
        query = query.filter(Booking.user_id == user_id)
    return query.all()

@router.post("/", response_model=BookingOut, status_code=201)
def create_booking(data: BookingCreate, db: Session = Depends(get_db)):
    """Neuen Sitzplatz buchen"""
    # Sitzplatz existiert?
    seat = db.query(Seat).filter(Seat.id == data.seat_id).first()
    if not seat:
        raise HTTPException(status_code=404, detail="Sitzplatz nicht gefunden")

    # Doppelbuchung abfangen (zusätzlich zum DB-Constraint)
    existing = db.query(Booking).filter(
        Booking.seat_id == data.seat_id,
        Booking.date == data.date
    ).first()
    if existing:
        raise HTTPException(
            status_code=409,
            detail="Dieser Sitzplatz ist an diesem Tag bereits gebucht"
        )

    booking = Booking(**data.model_dump())
    try:
        db.add(booking)
        db.commit()
        db.refresh(booking)
        return booking
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Dieser Sitzplatz ist an diesem Tag bereits gebucht"
        )

@router.delete("/{booking_id}", status_code=204)
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    """Buchung stornieren"""
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Buchung nicht gefunden")
    db.delete(booking)
    db.commit()