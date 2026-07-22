from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    title = Column(String)
    content_hash = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class PageVersion(Base):
    __tablename__ = "page_versions"

    id = Column(Integer, primary_key=True)
    page_id = Column(Integer, ForeignKey("pages.id"))

    content = Column(Text)

    version = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)
