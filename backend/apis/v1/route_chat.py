from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from db.session import get_db
from db.repository.chat import fetch_sessionshistory
from db.models.chat import Chat
from db.repository.chat import post_query
from schemas.chat import CreateChat


router = APIRouter()

#function to get sessions
@router.get("/get-session-history/user_id={user_id}&session_id={session_id}", status_code=status.HTTP_200_OK)
def fetch_sessions(user_id:int , session_id:int, db: Session= Depends(get_db)):
        chats = fetch_sessionshistory(user_id= user_id, session_id = session_id, db=db)
        return chats
 

#function to post query
@router.post("/post-query", status_code=status.HTTP_201_CREATED)
def post_the_query(chat: CreateChat, db: Session= Depends(get_db)):
    chat= post_query(chat=chat, db=db)
    return chat

    

