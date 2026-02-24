# Technische Dokumentation – Office Booking System (Backend)

## Inhaltsverzeichnis

1. [[#1-Überblick]]
2. [Technologie-Stack](#2-technologie-stack)
3. [Projektstruktur](#3-projektstruktur)
4. [Authentifizierung](#5-authentifizierung)
5. [API-Endpunkte](#6-api-endpunkte)
6. [Datenbank](#7-datenbank)
7. [Tests](#8-tests)
8. [Server starten](#9-server-starten)

---

## 1. Überblick

Das Backend des **Office Booking Systems** ist eine REST-API, die es Nutzern ermöglicht, Sitzplätze in Bürogebäuden zu buchen. Die Hierarchie lautet:

```
Gebäude (Building)
  └── Etage (Floor)
        └── Raum (Room)
              └── Sitzplatz (Seat)
                    └── Buchung (Booking)
```

---

## 2. Technologie-Stack

| Komponente      | Technologie              | Version  |
|-----------------|--------------------------|----------|
| Web-Framework   | FastAPI                  | 0.115.0  |
| ASGI-Server     | Uvicorn                  | 0.30.6   |
| ORM             | SQLAlchemy               | 2.0.35   |
| Validierung     | Pydantic                 | 2.9.2    |
| Authentifizierung | python-jose (JWT) + passlib (bcrypt) | 3.3.0 / 1.7.4 |
| Datenbank       | SQLite (Datei)           | –        |
| Test-Framework  | pytest                   | 8.3.2    |

---

## 3. Projektstruktur

```
backend/
├── main.py                  # App-Einstiegspunkt, Router-Registrierung, CORS
├── requirement.txt          # Abhängigkeiten
├── office_booking.db        # SQLite-Datenbankdatei (wird automatisch erstellt)
│
├── app/
│   ├── api/                 # HTTP-Endpunkte (Router)
│   │   ├── auth.py          # Registrierung, Login, /me
│   │   ├── buildings.py     # Gebäude CRUD
│   │   ├── floors.py        # Etagen CRUD
│   │   ├── rooms.py         # Räume CRUD
│   │   ├── seats.py         # Sitzplätze CRUD
│   │   └── bookings.py      # Buchungen erstellen / löschen / abfragen
│   │
│   ├── auth/
│   │   └── utils.py         # Passwort-Hashing, JWT-Erzeugung, Token-Validierung
│   │
│   ├── db/
│   │   └── db.py            # Engine, Session, Base, init_db(), Seed-Daten
│   │
│   └── models/              # SQLAlchemy-ORM-Modelle
│       ├── user.py
│       ├── building.py
│       ├── floor.py
│       ├── room.py
│       ├── seat.py
│       └── booking.py
│
└── tests/
    ├── conftest.py          # pytest-Fixtures (In-Memory-DB, TestClient)
    ├── test_auth_utils.py   # Unit-Tests für auth/utils.py
    └── test_bookings.py     # (noch nicht implementiert)
```

---


## 4. Authentifizierung

Das System verwendet **JWT (JSON Web Tokens)** mit dem HS256-Algorithmus.

### Ablauf

```
1. POST /api/auth/register  oder  POST /api/auth/login
        │
        ▼
   Passwort wird mit bcrypt verifiziert / gehasht
        │
        ▼
   JWT wird erzeugt (Payload: { sub: user_id, exp: +60 min })
        │
        ▼
   Token wird im Response zurückgegeben
        │
        ▼
   Client sendet Token im Header: Authorization: Bearer <token>
        │
        ▼
   get_current_user() validiert Token und gibt User zurück
```

### Wichtige Parameter (`app/auth/utils.py`)

| Parameter                    | Wert                            |
|------------------------------|---------------------------------|
| Algorithmus                  | HS256                           |
| Token-Gültigkeit             | 60 Minuten                      |
| Passwort-Hashing             | bcrypt via passlib               |

### Endpunkte

| Methode | Pfad               | Beschreibung                          | Auth erforderlich |
|---------|--------------------|---------------------------------------|-------------------|
| POST    | `/api/auth/register` | Neuen Nutzer registrieren           | Nein              |
| POST    | `/api/auth/login`    | Einloggen, Token erhalten           | Nein              |
| GET     | `/api/auth/me`       | Eingeloggten Nutzer abfragen        | Ja                |

---

## 6. API-Endpunkte

Basis-URL: `http://localhost:8001`

Die interaktive API-Dokumentation ist verfügbar unter:
`http://localhost:8001/docs` (Swagger UI)
`http://localhost:8001/redoc` (ReDoc)

### Buildings `/api/buildings`

| Methode | Pfad                   | Beschreibung              | Status |
|---------|------------------------|---------------------------|--------|
| GET     | `/`                    | Alle Gebäude abrufen      | 200    |
| GET     | `/{building_id}`       | Ein Gebäude abrufen       | 200    |
| POST    | `/`                    | Gebäude erstellen         | 201    |
| DELETE  | `/{building_id}`       | Gebäude löschen           | 204    |

**Request-Body (POST):**
```json
{ "name": "Gebäude A", "image_url": null }
```

### Floors `/api/floors`

| Methode | Pfad             | Query-Parameter  | Beschreibung              |
|---------|------------------|------------------|---------------------------|
| GET     | `/`              | `building_id`    | Etagen abrufen (optional gefiltert) |
| GET     | `/{floor_id}`    | –                | Eine Etage abrufen        |
| POST    | `/`              | –                | Etage erstellen           |
| DELETE  | `/{floor_id}`    | –                | Etage löschen             |

**Request-Body (POST):**
```json
{ "building_id": 1, "name": "Erdgeschoss", "floor_number": 0 }
```

### Rooms `/api/rooms`

| Methode | Pfad           | Query-Parameter | Beschreibung              |
|---------|----------------|-----------------|---------------------------|
| GET     | `/`            | `floor_id`      | Räume abrufen             |
| GET     | `/{room_id}`   | –               | Einen Raum abrufen        |
| POST    | `/`            | –               | Raum erstellen            |
| DELETE  | `/{room_id}`   | –               | Raum löschen              |

**Request-Body (POST):**
```json
{ "floor_id": 1, "name": "Raum 101", "room_number": "101", "capacity": 6 }
```



## 6. Datenbank

### Verbindung

Die Datenbank wird als SQLite-Datei gespeichert:

```
backend/office_booking.db
```

Die Verbindungs-URL lautet: `sqlite:///./office_booking.db`

### Initialisierung & Seed-Daten

Beim Start der Anwendung (`on_startup`) wird `init_db()` aufgerufen:

1. Alle Tabellen werden automatisch erstellt (falls nicht vorhanden)
2. Falls die Datenbank leer ist, werden Seed-Daten eingefügt:
   - 1 Test-User (`test@example.com` / `test123`)
   - 2 Gebäude (Building A, Building B)
   - 3 Etagen
   - 4 Räume (Kapazität 4–8)
   - Alle Sitzplätze entsprechend der Raumkapazität

### Session-Management

Jede HTTP-Anfrage erhält eine eigene Datenbank-Session über die FastAPI-Dependency `get_db()`. Die Session wird nach der Anfrage automatisch geschlossen.

---

## 7. Tests

### Ausführen

```bash
# Im Verzeichnis backend/
pytest                          # Alle Tests
pytest -v                       # Mit Details
pytest tests/test_auth_utils.py # Nur Auth-Tests
```

### Test-Infrastruktur (`tests/conftest.py`)

Die Tests verwenden eine **In-Memory-SQLite-Datenbank**, die nach jedem Test vollständig zurückgesetzt wird. Dadurch:
- sind Tests voneinander isoliert
- wird keine Produktionsdatenbank berührt
- laufen Tests schnell und ohne Seiteneffekte

**Fixtures:**

| Fixture  | Beschreibung                                                      |
|----------|-------------------------------------------------------------------|
| `db`     | Erzeugt alle Tabellen, liefert eine Session, räumt danach auf    |
| `client` | `TestClient` der FastAPI-App mit überschriebener `get_db`-Dependency |

### Vorhandene Tests (`tests/test_auth_utils.py`)

Unit-Tests für die reinen Hilfsfunktionen in `app/auth/utils.py` – kein HTTP, keine Datenbank:

| Test                                      | Prüft                                              |
|-------------------------------------------|----------------------------------------------------|
| `test_password_is_not_stored_as_plaintext` | Hash ≠ Klartext-Passwort                          |
| `test_hash_is_not_empty`                  | Hash hat ausreichende Länge                        |
| `test_same_password_produces_different_hashes` | bcrypt erzeugt immer neuen Salt              |
| `test_correct_password_is_accepted`       | `verify_password()` → `True` bei korrektem Passwort |
| `test_wrong_password_is_rejected`         | `verify_password()` → `False` bei falschem Passwort |
| `test_empty_password_is_handled_correctly`| Leeres Passwort wird korrekt behandelt             |
| `test_token_is_a_string`                  | Token ist ein nicht-leerer String                  |
| `test_token_contains_user_id`             | `sub`-Claim im JWT vorhanden                       |
| `test_token_contains_expiry`              | `exp`-Claim im JWT vorhanden                       |
| `test_different_user_ids_produce_different_tokens` | Verschiedene User → verschiedene Tokens  |

---

## 8. Server starten

### Voraussetzungen

```bash
pip install -r requirement.txt
```

### Entwicklungsserver

```bash
# Im Verzeichnis backend/
uvicorn main:app --reload --port 8001
```

Der Server läuft dann auf: `http://localhost:8001`

### CORS

Das Backend erlaubt Anfragen vom Vite-Dev-Server (`http://localhost:5173`).
Für andere Frontends muss `allow_origins` in [main.py](main.py) angepasst werden.
