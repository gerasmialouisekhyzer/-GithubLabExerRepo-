import os
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import IndexModel, ASCENDING
from bson import ObjectId

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "sharetray_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "donations")

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]

donation_collection = database[COLLECTION_NAME]
users_collection = database["users"]
audit_logs = database["audit_logs"]

index1 = IndexModel([("donor_id", ASCENDING), ("status", ASCENDING)], name="donor_status_idx")
index2 = IndexModel([("created_at", ASCENDING)], name="created_at_idx")

audit_index_ts = IndexModel([("timestamp", ASCENDING)], name="audit_ts_idx")
audit_index_actor = IndexModel([("actor_id", ASCENDING)], name="audit_actor_idx")

async def init_db():
  
    await donation_collection.create_indexes([index1, index2])
    await audit_logs.create_indexes([audit_index_ts, audit_index_actor])
    logger.info(f"✅ Created indexes on collection '{COLLECTION_NAME}' in database '{DB_NAME}'")
    logger.info(f"✅ Created indexes on collection 'audit_logs' in database '{DB_NAME}'")

async def close_db():

    client.close()
    logger.info("🔌 Closed MongoDB connection")

async def insert_donation(doc: dict) -> dict:
    result = await donation_collection.insert_one(doc)
    new_doc = await donation_collection.find_one({"_id": result.inserted_id})
    new_doc["id"] = str(new_doc["_id"])
    return new_doc

async def find_all_donations(skip: int = 0, limit: int = 100) -> list[dict]:
    cursor = donation_collection.find().skip(skip).limit(limit)
    docs = []
    async for d in cursor:
        d["id"] = str(d["_id"])
        docs.append(d)
    return docs

async def find_donation_by_id(donation_id: str) -> dict | None:
    doc = await donation_collection.find_one({"_id": ObjectId(donation_id)})
    if doc:
        doc["id"] = str(doc["_id"])
    return doc

async def update_donation_by_id(donation_id: str, update_data: dict) -> dict | None:
    result = await donation_collection.update_one({"_id": ObjectId(donation_id)}, {"$set": update_data})
    if result.modified_count == 1:
        updated = await donation_collection.find_one({"_id": ObjectId(donation_id)})
        updated["id"] = str(updated["_id"])
        return updated
    return None

async def delete_donation_by_id(donation_id: str) -> bool:
    result = await donation_collection.delete_one({"_id": ObjectId(donation_id)})
    return (result.deleted_count == 1)
