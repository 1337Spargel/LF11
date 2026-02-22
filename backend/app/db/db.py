from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///./buero_buchung.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Nötig für SQLite mit FastAPI
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    """Dependency: Datenbankverbindung pro Request"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Alle Tabellen erstellen beim Start"""
    from app.models import building, floor, room, seat, booking, user  # noqa
    Base.metadata.create_all(bind=engine)
    _seed_data()

def _seed_data():
    """Testdaten einfügen falls DB leer"""
    from app.models.building import Building
    from app.models.floor import Floor
    from app.models.room import Room
    from app.models.seat import Seat

    db = SessionLocal()
    try:
        if db.query(Building).count() > 0:
            return  # Bereits befüllt

        # Gebäude
        b1 = Building(name="Gebäude A")
        b2 = Building(name="Gebäude B")
        db.add_all([b1, b2])
        db.flush()

        # Etagen
        floors = [
            Floor(building_id=b1.id, name="Erdgeschoss", floor_number=0),
            Floor(building_id=b1.id, name="1. Obergeschoss", floor_number=1),
            Floor(building_id=b2.id, name="Erdgeschoss", floor_number=0),
        ]
        db.add_all(floors)
        db.flush()

        # Räume
        rooms = [
            Room(floor_id=floors[0].id, name="Raum 101", room_number="101", capacity=6),
            Room(floor_id=floors[0].id, name="Raum 102", room_number="102", capacity=4),
            Room(floor_id=floors[1].id, name="Raum 201", room_number="201", capacity=8),
            Room(floor_id=floors[2].id, name="Raum B-01", room_number="B01", capacity=5),
        ]
        db.add_all(rooms)
        db.flush()

        # Sitzplätze
        seats = []
        for room in rooms:
            for i in range(1, room.capacity + 1):
                seats.append(Seat(room_id=room.id, seat_number=str(i)))
        db.add_all(seats)

        db.commit()
        print("Testdaten erfolgreich eingefügt")
    except Exception as e:
        db.rollback()
        print(f"Fehler beim Seeden: {e}")
    finally:
        db.close()