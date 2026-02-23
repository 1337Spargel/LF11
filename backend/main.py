from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.db import init_db
from app.api import buildings, floors, rooms, seats, bookings, auth

app = FastAPI(title="Office Booking System API", version="1.0.0")

# CORS – allow the React frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database on startup
@app.on_event("startup")
def on_startup():
    init_db()

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(buildings.router, prefix="/api/buildings", tags=["Buildings"])
app.include_router(floors.router, prefix="/api/floors", tags=["Floors"])
app.include_router(rooms.router, prefix="/api/rooms", tags=["Rooms"])
app.include_router(seats.router, prefix="/api/seats", tags=["Seats"])
app.include_router(bookings.router, prefix="/api/bookings", tags=["Bookings"])

@app.get("/")
def root():
    return {"message": "Office Booking System API is running!"}