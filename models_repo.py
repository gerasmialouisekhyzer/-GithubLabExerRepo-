from typing import List, Optional, Dict, Any, Tuple
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
import uuid
import json
import os

def gen_id() -> str:
    return str(uuid.uuid4())

# Enumerations and Models
class Role(str, Enum):
    DONOR = "donor"
    RECIPIENT = "recipient"
    VOLUNTEER = "volunteer"
    ADMIN = "admin"

class Perishability(str, Enum):
    FRESH = "fresh"
    REFRIGERATED = "refrigerated"
    STABLE = "stable"

class DonationState(str, Enum):
    POSTED = "posted"
    MATCHED = "matched"
    PICKUP_SCHEDULED = "pickup_scheduled"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    EXPIRED = "expired"

class User(BaseModel):
    id: str = Field(default_factory=gen_id)
    name: str
    role: Role
    phone: Optional[str] = None
    # GeoJSON: {"type":"Point","coordinates":[lon,lat]}
    location: Optional[Dict[str, float]] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

class FoodItem(BaseModel):
    id: str = Field(default_factory=gen_id)
    name: str
    quantity: int = 1
    approximate_weight_kg: float = 0.5
    perishability: Perishability = Perishability.STABLE
    notes: Optional[str] = None

class Donation(BaseModel):
    id: str = Field(default_factory=gen_id)
    donor_id: str
    items: List[FoodItem]
    total_weight_kg: float
    posted_at: datetime = Field(default_factory=datetime.utcnow)
    pickup_by: Optional[datetime] = None
    location: Optional[Dict[str, Any]] = None  # GeoJSON
    state: DonationState = DonationState.POSTED
    matched_recipient_id: Optional[str] = None
    pickup_id: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

class Recipient(BaseModel):
    id: str = Field(default_factory=gen_id)
    name: str
    capacity_kg: float
    location: Optional[Dict[str, float]] = None
    contact: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

class Pickup(BaseModel):
    id: str = Field(default_factory=gen_id)
    volunteer_id: Optional[str] = None
    donation_ids: List[str] = Field(default_factory=list)
    route_order: List[Tuple[float, float]] = Field(default_factory=list)  # (lat, lon) tuples
    scheduled_for: Optional[datetime] = None
    status: str = "scheduled"
    metadata: Dict[str, Any] = Field(default_factory=dict)

class Transaction(BaseModel):
    id: str = Field(default_factory=gen_id)
    donation_id: str
    recipient_id: str
    picked_up_at: Optional[datetime] = None
    delivered_at: Optional[datetime] = None
    notes: Optional[str] = None

class AuditLogEntry(BaseModel):
    id: str = Field(default_factory=gen_id)
    donation_id: str
    actor_user_id: Optional[str] = None
    actor_role: Optional[Role] = None
    old_state: Optional[DonationState] = None
    new_state: DonationState
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    notes: Optional[str] = None

# In-Memory Repository
class InMemoryRepo:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.donations: Dict[str, Donation] = {}
        self.recipients: Dict[str, Recipient] = {}
        self.pickups: Dict[str, Pickup] = {}
        self.transactions: Dict[str, Transaction] = {}
        self.audit_logs: Dict[str, List[AuditLogEntry]] = {}

    # Users
    def add_user(self, u: User) -> User:
        self.users[u.id] = u
        return u

    def get_user(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)

    # Donations
    def add_donation(self, d: Donation) -> Donation:
        self.donations[d.id] = d
        return d

    def get_donation(self, donation_id: str) -> Optional[Donation]:
        return self.donations.get(donation_id)

    def update_donation(self, d: Donation) -> Donation:
        if d.id not in self.donations:
            raise KeyError("Donation not found")
        self.donations[d.id] = d
        return d

    def list_open_donations(self) -> List[Donation]:
        return [d for d in self.donations.values() if d.state == DonationState.POSTED]

    # Recipients
    def add_recipient(self, r: Recipient) -> Recipient:
        self.recipients[r.id] = r
        return r

    def list_recipients(self) -> List[Recipient]:
        return list(self.recipients.values())

    def update_recipient(self, r: Recipient) -> Recipient:
        if r.id not in self.recipients:
            raise KeyError("Recipient not found")
        self.recipients[r.id] = r
        return r

    def get_recipient(self, recipient_id: str) -> Optional[Recipient]:
        return self.recipients.get(recipient_id)

    # Pickups
    def add_pickup(self, p: Pickup) -> Pickup:
        self.pickups[p.id] = p
        return p

    def update_pickup(self, p: Pickup) -> Pickup:
        if p.id not in self.pickups:
            raise KeyError("Pickup not found")
        self.pickups[p.id] = p
        return p

    # Transactions
    def add_transaction(self, t: Transaction) -> Transaction:
        self.transactions[t.id] = t
        return t

    # Audit Logs
    def add_audit_log(self, log: AuditLogEntry) -> AuditLogEntry:
        self.audit_logs.setdefault(log.donation_id, []).append(log)
        return log

    def get_audit_logs_for_donation(self, donation_id: str) -> List[AuditLogEntry]:
        return self.audit_logs.get(donation_id, [])

# MongoDB Adapter (PyMongo)
try:
    from pymongo import MongoClient, ASCENDING, GEOSPHERE
    PYMONGO_AVAILABLE = True
except Exception:
    PYMONGO_AVAILABLE = False

class MongoRepo:
    def __init__(self, uri: str = None, db_name: str = None):
        if not PYMONGO_AVAILABLE:
            raise RuntimeError("pymongo is required for MongoRepo. Install with `pip install pymongo`.")
        uri = uri or os.environ.get("MONGO_URI", "mongodb://localhost:27017")
        db_name = db_name or os.environ.get("MONGO_DB", "sharetray")
        client = MongoClient(uri)
        db = client[db_name]
        self.users = db["users"]
        self.donations = db["donations"]
        self.recipients = db["recipients"]
        self.pickups = db["pickups"]
        self.transactions = db["transactions"]
        self.audit_logs = db["audit_logs"]
        
        try:
            self.recipients.create_index([("location", GEOSPHERE)])
            self.donations.create_index([("state", ASCENDING), ("pickup_by", ASCENDING)])
        except Exception:
            pass

    # Users
    def add_user(self, u: User) -> User:
        self.users.insert_one(u.dict())
        return u
    def get_user(self, user_id: str) -> Optional[User]:
        d = self.users.find_one({"id": user_id})
        return User(**d) if d else None

    # Donations
    def add_donation(self, d: Donation) -> Donation:
        self.donations.insert_one(d.dict())
        return d
    def get_donation(self, donation_id: str) -> Optional[Donation]:
        d = self.donations.find_one({"id": donation_id})
        return Donation(**d) if d else None
    def update_donation(self, d: Donation) -> Donation:
        res = self.donations.replace_one({"id": d.id}, d.dict(), upsert=False)
        if getattr(res, "matched_count", 0) == 0:
            raise KeyError("Donation not found")
        return d
    def list_open_donations(self):
        docs = self.donations.find({"state": DonationState.POSTED.value})
        return [Donation(**doc) for doc in docs]

    # Recipients
    def add_recipient(self, r: Recipient) -> Recipient:
        self.recipients.insert_one(r.dict()); return r
    def list_recipients(self): return [Recipient(**d) for d in self.recipients.find()]
    def update_recipient(self, r: Recipient): self.recipients.replace_one({"id": r.id}, r.dict()); return r
    def get_recipient(self, recipient_id: str) -> Optional[Recipient]:
        d = self.recipients.find_one({"id": recipient_id})
        return Recipient(**d) if d else None

    # Pickups/Transactions/Audit
    def add_pickup(self, p: Pickup): self.pickups.insert_one(p.dict()); return p
    def update_pickup(self, p: Pickup): self.pickups.replace_one({"id": p.id}, p.dict()); return p
    def add_transaction(self, t: Transaction): self.transactions.insert_one(t.dict()); return t
    def add_audit_log(self, log: AuditLogEntry): self.audit_logs.insert_one(log.dict()); return log
    def get_audit_logs_for_donation(self, donation_id: str):
        docs = self.audit_logs.find({"donation_id": donation_id}).sort("timestamp", 1)
        return [AuditLogEntry(**d) for d in docs]

# Single Repo Instance
if os.environ.get("MONGO_URI") and PYMONGO_AVAILABLE:
    repo = MongoRepo()
else:
    repo = InMemoryRepo()

# Small Demo Seed
def seed_demo() -> Dict[str, str]:
    donor = repo.add_user(User(name="Demo Donor", role=Role.DONOR, location={"type":"Point","coordinates":[121.001,14.601]}))
    recipient = repo.add_recipient(Recipient(name="Demo Pantry", capacity_kg=100.0, location={"type":"Point","coordinates":[121.005,14.605]}, contact="09170000000"))
    volunteer = repo.add_user(User(name="Demo Volunteer", role=Role.VOLUNTEER, location={"type":"Point","coordinates":[121.002,14.603]}))
    item = FoodItem(name="Cooked Rice", quantity=10, approximate_weight_kg=5.0, perishability=Perishability.FRESH)
    donation = repo.add_donation(Donation(donor_id=donor.id, items=[item], total_weight_kg=5.0, location={"type":"Point","coordinates":[121.0015,14.602]}))
    return {"donor_id": donor.id, "recipient_id": recipient.id, "volunteer_id": volunteer.id, "donation_id": donation.id}

# Quick JSON-print helper
def dump_repo_state(path: str = "repo_state.json"):
    out = {
        "users": [u.dict() for u in repo.users.values()] if isinstance(repo, InMemoryRepo) else [],
        "donations": [d.dict() for d in repo.donations.values()] if isinstance(repo, InMemoryRepo) else [],
        "recipients": [r.dict() for r in repo.recipients.values()] if isinstance(repo, InMemoryRepo) else [],
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, default=str, indent=2)

if __name__ == "__main__":
    ids = seed_demo()
    print("Seeded demo IDs:", ids)
    dump_repo_state()
