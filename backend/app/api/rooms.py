from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.db.db import get_db
from app.models.room import Room

router = APIRouter()

class RoomOut(BaseModel):
    id: int
    floor_id: int
    name: str
    room_number: str
    capacity: int

    class Config:
        from_attributes = True

class RoomCreate(BaseModel):
    floor_id: int
    name: str
    room_number: str
    capacity: int

@router.get("/", response_model=list[RoomOut])
def get_rooms(floor_id: int | None = None, db: Session = Depends(get_db)):
    query = db.query(Room)
    if floor_id:
        query = query.filter(Room.floor_id == floor_id)
    return query.all()

@router.get("/{room_id}", response_model=RoomOut)
def get_room(room_id: int, db: Session = Depends(get_db)):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Raum nicht gefunden")
    return room

@router.post("/", response_model=RoomOut, status_code=201)
def create_room(data: RoomCreate, db: Session = Depends(get_db)):
    room = Room(**data.model_dump())
    db.add(room)
    db.commit()
    db.refresh(room)
    return room

@router.delete("/{room_id}", status_code=204)
def delete_room(room_id: int, db: Session = Depends(get_db)):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Raum nicht gefunden")
    db.delete(room)
    db.commit()
