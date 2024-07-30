from motor.motor_asyncio import AsyncIOMotorClient
from .core.config import settings
from pydantic import BaseModel

class DocumentManager:
    def __init__(self, client_session: AsyncIOMotorClient, database_name: str, collection_name: str) -> None:
        self.database = database_name
        self.collection = collection_name
        self.client = client_session
        pass

    async def create_document(self, pydantic_model: BaseModel):
        try:
            document = pydantic_model.model_dump()
            result = await self.collection.insert_one(document)
            return print(f"Document inserted with ID: {result.inserted_id}")
        except Exception as e:
            print(f"Failed to create document: {e}")

    async def get_single_document(self):
        try:
        except Exception as e:
            print(f"Failed to get document {document_name}: {e}")

    async def get_multiple_document(self):
        try:
        except Exception as e:
            print(f"Failed to get document {document_name}: {e}")

    async def update_document(self):
        try:
        except Exception as e:
            print(f"Failed to update document {document_name}: {e}")

    async def delete_document(self):
        try:
        except Exception as e:
            print(f"Failed to delete document {document_name}: {e}")