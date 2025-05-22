from fastapi import APIRouter
from apis.v1 import route_user
from apis.v1 import route_session
from apis.v1 import route_chat

#calling the APIRouter
api_router=APIRouter()

api_router.include_router(route_user.router , tags=["users"])
api_router.include_router(route_session.router , tags=["sessions"])
api_router.include_router(route_chat.router , tags=["sessionsHistory"])

