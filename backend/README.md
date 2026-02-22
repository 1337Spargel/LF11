# Backend – Bürobuchungssystem

## Setup

```bash
# Im backend/ Ordner:
pip install -r requirement.txt

# Server starten:
uvicorn main:app --reload
```

## API Dokumentation
Nach dem Start erreichbar unter:
- Swagger UI: http://localhost:8000/docs
- ReDoc:       http://localhost:8000/redoc

## Endpunkte

| Method | URL                        | Beschreibung                          |
|--------|----------------------------|---------------------------------------|
| GET    | /api/buildings             | Alle Gebäude                          |
| GET    | /api/buildings/{id}        | Ein Gebäude                           |
| GET    | /api/floors?building_id=1  | Etagen (gefiltert nach Gebäude)       |
| GET    | /api/rooms?floor_id=1      | Räume (gefiltert nach Etage)          |
| GET    | /api/seats?room_id=1&check_date=2025-03-01 | Sitzplätze mit Verfügbarkeit |
| POST   | /api/bookings              | Buchung erstellen                     |
| DELETE | /api/bookings/{id}         | Buchung stornieren                    |

## Projektstruktur

```
backend/
├── main.py                  # Einstiegspunkt
├── requirements.txt
└── app/
    ├── api/                 # Endpunkte
    │   ├── buildings.py
    │   ├── floors.py
    │   ├── rooms.py
    │   ├── seats.py
    │   └── bookings.py
    ├── models/              # Datenbankmodelle
    │   ├── building.py
    │   ├── floor.py
    │   ├── room.py
    │   ├── seat.py
    │   ├── booking.py
    │   └── user.py
    ├── database/
    │   └── db.py            # SQLite Setup + Testdaten
    ├── services/            # (Geschäftslogik – kommt später)
    └── repositories/        # (DB-Zugriff – kommt später)
```