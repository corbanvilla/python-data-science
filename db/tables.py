"""
This module defines the tables used in the database.

It can be used as a helpful reference for the database schema.
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Double,
    ForeignKey,
    Text,
    JSON,
    Numeric,
    ARRAY,
    DateTime,
    UniqueConstraint,
    CheckConstraint,
    LargeBinary,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime, timezone

# Define a base class
Base = declarative_base()


class ExampleTable1(Base):
    __tablename__ = "example_table_1"
    id = Column(Integer, primary_key=True)

    name = Column(String(100), unique=True)
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    items = relationship("ExampleTable2", backref="parent")


class ExampleTable2(Base):
    __tablename__ = "example_table_2"
    id = Column(Integer, primary_key=True)

    title = Column(String(200))
    content = Column(Text)
    priority = Column(Integer)

    # Foreign keys
    parent_id = Column(Integer, ForeignKey("example_table_1.id"))
