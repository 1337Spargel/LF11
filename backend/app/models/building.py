from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.db import Base

class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    image_url = Column(String, nullable=True)

    floors = relationship("Floor", back_populates="building", cascade="all, delete")