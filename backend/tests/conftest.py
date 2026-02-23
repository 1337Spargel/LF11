"""
Shared test fixtures for all tests.

conftest.py is loaded automatically by pytest – no imports needed.
A fresh in-memory SQLite database is created for each test and
dropped afterwards so tests do not interfere with each other.
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.db import Base, get_db
from main import app

# In-memory SQLite – only exists during the test, no file on disk
TEST_DB_URL = "sqlite:///:memory:"

test_engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
TestSession = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture()
def db():
    """Creates all tables, provides a session, and cleans up afterwards."""
    Base.metadata.create_all(bind=test_engine)
    session = TestSession()
    yield session
    session.close()
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture()
def client(db):
    """
    HTTP test client for the FastAPI app.
    The get_db dependency is redirected to the test database
    so no real database file is touched.
    """
    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)  # no 'with' → no startup event → no init_db()
    app.dependency_overrides.clear()
