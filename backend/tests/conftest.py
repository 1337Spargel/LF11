"""
Gemeinsame Test-Fixtures für alle Tests.

conftest.py wird von pytest automatisch geladen – keine Imports nötig.
Hier wird eine frische In-Memory-SQLite-Datenbank für jeden Test aufgebaut
und danach wieder geleert, damit Tests sich nicht gegenseitig beeinflussen.
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.db import Base, get_db
from main import app

# In-Memory-SQLite – existiert nur während des Tests, keine Datei auf der Festplatte
TEST_DB_URL = "sqlite:///:memory:"

test_engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
TestSession = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture()
def db():
    """Erstellt alle Tabellen, liefert eine Session, räumt danach auf."""
    Base.metadata.create_all(bind=test_engine)
    session = TestSession()
    yield session
    session.close()
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture()
def client(db):
    """
    HTTP-Testclient der FastAPI-App.
    Die get_db-Dependency wird auf die Test-DB umgeleitet,
    damit kein echter Datenbankfile berührt wird.
    """
    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)  # kein 'with' → kein startup-Event → kein init_db()
    app.dependency_overrides.clear()
