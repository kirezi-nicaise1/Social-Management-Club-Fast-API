from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Member(Base):
    __tablename__ = 'members'
    member_id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(100), unique=True, index=True)
    email=Column(String(100),nullable=False,unique=True)
    membership_type = Column(String(100), default='regular' ,nullable=True)
    registration_date = Column(DateTime, default=func.now())

    event = relationship("Event", back_populates="member")

    def __str__(self):
        return self.name

class Event(Base):
    __tablename__ = 'events'
    event_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(80), index=True)
    description = Column(Text)
    location=Column(String(100))
    member_id = Column(Integer, ForeignKey('members.member_id'), nullable=False)
    

    member = relationship("Member", back_populates="event")

    def __str__(self):
        return self.title
