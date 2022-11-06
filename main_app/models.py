from database.base import Base
from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    Column,
    DateTime
)


class BlackList(Base):
    __tablename__ = 'black_list'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    address = Column(String, unique=True)
    ban_duration = Column(Integer)
    ban_start = Column(DateTime, default=datetime.now())
