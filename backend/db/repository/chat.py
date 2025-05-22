from schemas.chat import CreateChat
from sqlalchemy.orm import session
from datetime import datetime
from db.models.chat import Chat
# from fastapi import exceptions
from Agent import agent_executor
from functools import wraps

def rate_limited(max_calls=10, period=60):  # 10 calls per minute
    def decorator(func):
        calls = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            calls = [t for t in calls if t > datetime.now().timestamp() - period]
            if len(calls) >= max_calls:
                raise RuntimeError("Rate limit exceeded")
            calls.append(datetime.now().timestamp())
            return func(*args, **kwargs)
        return wrapper
    return decorator


#function to post a query
@rate_limited()
def post_query(chat: CreateChat, db: session):
           try:
               chat_db=Chat(input_query = chat.input_query,
                     chatTimestamp = datetime.now(),
                     user_id = chat.user_id,
                     session_id = chat.session_id,
                     format=chat.format
               )     
               db.add(chat_db)
               print(chat_db.input_query)
               db.commit()
               db.refresh(chat_db)
               response= str(agent_executor.invoke({"input" : chat_db.input_query}))
        #    formatted_response = format_response(response, chat_db.format)
               response_db = Chat(output_query = response,input_query= chat.input_query, chatTimestamp = datetime.now(), user_id = chat.user_id, session_id = chat.session_id, format=chat.format)
               db.add(response_db)
               db.commit()
               db.refresh(response_db)
               return response_db
           except Exception as e:
                 db.rollback()
                 raise e
        #    return Chat.from_orm(response_db)


#function to fetch session_history
def fetch_sessionshistory(user_id : int, session_id: int, db:session):
        chats = db.query(Chat).filter(Chat.user_id==user_id, Chat.session_id== session_id).all()
        return chats
        
    
     