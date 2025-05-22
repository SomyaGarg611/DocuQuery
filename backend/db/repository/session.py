from sqlalchemy.orm import session
from schemas.session import CreateSession
from db.models.session import Session

#function to create new sesssion
def create_new_session(session: CreateSession, db: session):
    session=Session(
        user_id=session.user_id,
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session

#function to fetch all the sessions of a user
def fetch_all_sessions(user_id:int, db: session):
    sessions = db.query(Session).filter(Session.user_id==user_id).all()
    return sessions