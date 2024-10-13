import os
from dotenv import load_dotenv
from datetime import datetime, timezone
from src.application.extensions.Management import db

load_dotenv()

schema = os.getenv('DATABASE_SCHEMA', 'public')

class BaseEntity(db.Model):
    __abstract__ = True
    __table_args__ = {'schema': schema}
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc))
