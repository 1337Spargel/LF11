from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import Base

class Seat(Base):
    __tablename__ = "seats"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    seat_number = Column(String, nullable=False)

    room = relationship("Room", back_populates="seats")
    bookings = relationship("Booking", back_populates="seat", cascade="all, delete")
