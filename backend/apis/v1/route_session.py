from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from schemas.session import CreateSession, ShowSession
from db.session import get_db
from db.repository.session import create_new_session
from db.repository.session import fetch_all_sessions

router = APIRouter()

#routing for create session
@router.post("/create-session", response_model=ShowSession, status_code=status.HTTP_201_CREATED)
def create_session(session:CreateSession, db: Session= Depends(get_db)):
    session= create_new_session(session=session, db=db )
    return session

#routing for get fessions
@router.get("/fetch-sessions/{id}", response_model=list[ShowSession], status_code=status.HTTP_200_OK)
def fetch_sessions(id:int, db: Session= Depends(get_db)):
    sessions = fetch_all_sessions(user_id=id, db=db )
    return sessions

