from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.db.db import get_db
from app.models.floor import Floor

router = APIRouter()

class FloorOut(BaseModel):
    id: int
    building_id: int
    name: str
    floor_number: int

    class Config:
        from_attributes = True

class FloorCreate(BaseModel):
    building_id: int
    name: str
    floor_number: int

@router.get("/", response_model=list[FloorOut])
def get_floors(building_id: int | None = None, db: Session = Depends(get_db)):
    query = db.query(Floor)
    if building_id:
        query = query.filter(Floor.building_id == building_id)
    return query.all()

@router.get("/{floor_id}", response_model=FloorOut)
def get_floor(floor_id: int, db: Session = Depends(get_db)):
    floor = db.query(Floor).filter(Floor.id == floor_id).first()
    if not floor:
        raise HTTPException(status_code=404, detail="Floor not found")
    return floor

@router.post("/", response_model=FloorOut, status_code=201)
def create_floor(data: FloorCreate, db: Session = Depends(get_db)):
    floor = Floor(**data.model_dump())
    db.add(floor)
    db.commit()
    db.refresh(floor)
    return floor

@router.delete("/{floor_id}", status_code=204)
def delete_floor(floor_id: int, db: Session = Depends(get_db)):
    floor = db.query(Floor).filter(Floor.id == floor_id).first()
    if not floor:
        raise HTTPException(status_code=404, detail="Floor not found")
    db.delete(floor)
    db.commit()
