from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.db import Base


class Sentiment(Base):
    __tablename__ = "sentiments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user_name = Column(String, nullable=False)
    comment = Column(String, nullable=False)
    sentiment = Column(String, nullable=False)  # positive / negative
    created_at = Column(DateTime, default=datetime.utcnow)

