from sqlalchemy import Column, Integer, String, ForeignKey, Date, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.db import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    seat_id = Column(Integer, ForeignKey("seats.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)

    # Verhindert Doppelbuchungen: gleicher Sitz am gleichen Tag
    __table_args__ = (
        UniqueConstraint("seat_id", "date", name="uq_seat_date"),
    )

    seat = relationship("Seat", back_populates="bookings")
    user = relationship("User", back_populates="bookings")