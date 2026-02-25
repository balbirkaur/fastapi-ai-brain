from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import db_manager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Connect to DB
    await db_manager.connect()
    yield
    # Shutdown: Clean up
    await db_manager.close()

app = FastAPI(title="AI Brain API", lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "API is live and DB is connected!"}