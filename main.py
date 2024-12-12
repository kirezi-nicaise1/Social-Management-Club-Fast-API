from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session # type: ignore
import models, schemas, crud
from connection import engine, SessionLocal



models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
    


@app.post("/members/", response_model=schemas.Member)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    return crud.create_member(db=db, member=member)

@app.get("/members/", response_model=list[schemas.Member])
def read_members(skip: int = 0, limit: int = 1000000, db: Session = Depends(get_db)):
    members = crud.get_members(db, skip=skip, limit=limit)
    return members

@app.get("/members/{member_id}", response_model=schemas.Member)
def read_member(member_id: int, db: Session = Depends(get_db)):
    member = crud.get_member(db=db, member_id=member_id)
    if member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

@app.put("/members/{member_id}", response_model=schemas.Member)
def update_member(member_id: int, updated_data: schemas.MemberUpdate, db: Session = Depends(get_db)):
    # updated_data_dict = updated_data.dict(exclude_unset=True)
    return crud.update_member(db=db, member_id=member_id, member_update=updated_data)

@app.delete("/members/{member_id}")
def delete_member(member_id: int, db: Session = Depends(get_db)):
    crud.delete_member(db=db, member_id=member_id)
    return {"message": "Member deleted successfully"}


# Event Endpoints

@app.post("/events/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db=db, event=event)

@app.get("/events/", response_model=list[schemas.Event])
def read_events(skip: int = 0, limit: int = 1000000, db: Session = Depends(get_db)):
    return crud.get_events(db=db, skip=skip, limit=limit)

@app.get("/events/{event_id}", response_model=schemas.Event)
def read_event(event_id: int, db: Session = Depends(get_db)):
    event = crud.get_event(db=db, event_id=event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@app.get("/events/title/{title}", response_model=schemas.Event)
def read_event_by_title(title: str, db: Session = Depends(get_db)):
    event = crud.get_event_by_title(db=db, title=title)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@app.put("/events/{event_id}", response_model=schemas.Event)
def update_event(event_id: int, updated_data: schemas.EventUpdate, db: Session = Depends(get_db)):
    return crud.update_event(db=db, event_id=event_id, event_update=updated_data)

@app.delete("/events/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    crud.delete_event(db=db, event_id=event_id)
    return {"message": "Event deleted successfully"}
