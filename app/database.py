from motor.motor_asyncio import AsyncIOMotorClient
import os

class DatabaseManager:
    """
    OOP Singleton: This class ensures we only have 
    ONE connection pool to MongoDB at a time.
    """
    client: AsyncIOMotorClient = None

    def __init__(self):
        # The URL points to the name we gave in docker-compose.yml
        self.mongo_url = "mongodb://localhost:27017"
        self.db_name = "ai_brain_db"

    async def connect(self):
        self.client = AsyncIOMotorClient(self.mongo_url)
        print("Successfully connected to MongoDB!")

    async def close(self):
        self.client.close()
        print("MongoDB connection closed.")

# Create an instance that we can import elsewhere
db_manager = DatabaseManager()