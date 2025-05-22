from sqlalchemy.orm import session
from schemas.user import UserCreate
from db.models.user import User
from core.hashing import Hasher

#function to craete new user
def create_new_user(user: UserCreate, db: session):
    user=User(
        email=user.email,
        password=Hasher.get_password_hash(user.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
