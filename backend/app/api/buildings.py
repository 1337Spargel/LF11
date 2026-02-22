from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.db.db import get_db
from app.models.building import Building

router = APIRouter()

class BuildingOut(BaseModel):
    id: int
    name: str
    image_url: str | None = None

    class Config:
        from_attributes = True

class BuildingCreate(BaseModel):
    name: str
    image_url: str | None = None

@router.get("/", response_model=list[BuildingOut])
def get_buildings(db: Session = Depends(get_db)):
    return db.query(Building).all()

@router.get("/{building_id}", response_model=BuildingOut)
def get_building(building_id: int, db: Session = Depends(get_db)):
    building = db.query(Building).filter(Building.id == building_id).first()
    if not building:
        raise HTTPException(status_code=404, detail="Gebäude nicht gefunden")
    return building

@router.post("/", response_model=BuildingOut, status_code=201)
def create_building(data: BuildingCreate, db: Session = Depends(get_db)):
    building = Building(**data.model_dump())
    db.add(building)
    db.commit()
    db.refresh(building)
    return building

@router.delete("/{building_id}", status_code=204)
def delete_building(building_id: int, db: Session = Depends(get_db)):
    building = db.query(Building).filter(Building.id == building_id).first()
    if not building:
        raise HTTPException(status_code=404, detail="Gebäude nicht gefunden")
    db.delete(building)
    db.commit()
