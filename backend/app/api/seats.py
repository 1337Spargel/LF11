from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.db.db import get_db
from app.models.seat import Seat

router = APIRouter()

class SeatOut(BaseModel):
    id: int
    room_id: int
    seat_number: str

    class Config:
        from_attributes = True

class SeatCreate(BaseModel):
    room_id: int
    seat_number: str

@router.get("/", response_model=list[SeatOut])
def get_seats(room_id: int | None = None, db: Session = Depends(get_db)):
    query = db.query(Seat)
    if room_id:
        query = query.filter(Seat.room_id == room_id)
    return query.all()

@router.get("/{seat_id}", response_model=SeatOut)
def get_seat(seat_id: int, db: Session = Depends(get_db)):
    seat = db.query(Seat).filter(Seat.id == seat_id).first()
    if not seat:
        raise HTTPException(status_code=404, detail="Sitzplatz nicht gefunden")
    return seat

@router.post("/", response_model=SeatOut, status_code=201)
def create_seat(data: SeatCreate, db: Session = Depends(get_db)):
    seat = Seat(**data.model_dump())
    db.add(seat)
    db.commit()
    db.refresh(seat)
    return seat

@router.delete("/{seat_id}", status_code=204)
def delete_seat(seat_id: int, db: Session = Depends(get_db)):
    seat = db.query(Seat).filter(Seat.id == seat_id).first()
    if not seat:
        raise HTTPException(status_code=404, detail="Sitzplatz nicht gefunden")
    db.delete(seat)
    db.commit()
