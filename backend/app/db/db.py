from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///./office_booking.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Required for SQLite with FastAPI
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    """Dependency: Database connection per request"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Create all tables on startup"""
    from app.models import building, floor, room, seat, booking, user  # noqa
    Base.metadata.create_all(bind=engine)
    _seed_data()

def _seed_data():
    """Insert seed data if database is empty"""
    from app.models.building import Building
    from app.models.floor import Floor
    from app.models.room import Room
    from app.models.seat import Seat
    from app.models.user import User
    from app.auth.utils import hash_password

    db = SessionLocal()
    try:
        if db.query(Building).count() > 0:
            return  # Already populated

        # Test user
        test_user = User(
            name="Test User",
            email="test@example.com",
            hashed_password=hash_password("test123"),
        )
        db.add(test_user)
        db.flush()

        # Buildings
        b1 = Building(name="Building A")
        b2 = Building(name="Building B")
        db.add_all([b1, b2])
        db.flush()

        # Floors
        floors = [
            Floor(building_id=b1.id, name="Ground Floor", floor_number=0),
            Floor(building_id=b1.id, name="1st Floor", floor_number=1),
            Floor(building_id=b2.id, name="Ground Floor", floor_number=0),
        ]
        db.add_all(floors)
        db.flush()

        # Rooms
        rooms = [
            Room(floor_id=floors[0].id, name="Room 101", room_number="101", capacity=6),
            Room(floor_id=floors[0].id, name="Room 102", room_number="102", capacity=4),
            Room(floor_id=floors[1].id, name="Room 201", room_number="201", capacity=8),
            Room(floor_id=floors[2].id, name="Room B-01", room_number="B01", capacity=5),
        ]
        db.add_all(rooms)
        db.flush()

        # Seats
        seats = []
        for room in rooms:
            for i in range(1, room.capacity + 1):
                seats.append(Seat(room_id=room.id, seat_number=str(i)))
        db.add_all(seats)

        db.commit()
        print("Seed data inserted successfully")
    except Exception as e:
        db.rollback()
        print(f"Error during seeding: {e}")
    finally:
        db.close()
