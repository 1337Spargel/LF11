from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import Base

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    floor_id = Column(Integer, ForeignKey("floors.id"), nullable=False)
    name = Column(String, nullable=False)
    room_number = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False, default=1)

    floor = relationship("Floor", back_populates="rooms")
    seats = relationship("Seat", back_populates="room", cascade="all, delete")
