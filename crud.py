from sqlalchemy.orm import Session 
from models import Member,Event
from schemas import MemberCreate, MemberUpdate, EventCreate, EventUpdate



def get_members(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Member).offset(skip).limit(limit).all()


def get_member(db: Session, member_id: int):
    return db.query(Member).filter(Member.member_id == member_id).first()

def create_member(db: Session, member: MemberCreate):
    db_member = Member(name=member.name, email=member.email,membership_type=member.membership_type)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def update_member(db: Session, member_id: int, member_update: MemberUpdate):
    db_member = db.query(Member).filter(Member.member_id == member_id).first()
    if not db_member:
        return None
    for key, value in member_update.dict(exclude_unset=True).items():
        setattr(db_member, key, value)
    db.commit()
    db.refresh(db_member)
    return db_member


def delete_member(db: Session, member_id: int):
    db_member = db.query(Member).filter(Member.member_id == member_id).first()
    if db_member:
        db.delete(db_member)
        db.commit()
        return db_member
    return None


# Events

def get_events(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Event).offset(skip).limit(limit).all()

def get_event(db: Session, event_id: int):
    return db.query(Event).filter(Event.event_id == event_id).first()


def create_event(db: Session, event: EventCreate):
    db_event = Event(
        title=event.title,
        member_id=event.member_id,
        location=event.location,
        description=event.description,
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def update_event(db: Session, event_id: int, event_update: EventUpdate):
    db_event = db.query(Event).filter(Event.event_id == event_id).first()
    if not db_event:
        return None
    for key, value in event_update.dict(exclude_unset=True).items():
        setattr(db_event, key, value)
    db.commit()
    db.refresh(db_event)
    return db_event


def delete_event(db: Session, event_id: int):
    db_event = db.query(Event).filter(Event.event_id == event_id).first()
    if db_event:
        db.delete(db_event)
        db.commit()
        return db_event
    return None

def get_event_by_name(db: Session, title: str):
    return db.query(Event).filter(Event.title == title).first()
