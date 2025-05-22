import os
import sys
from typing import Any
from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# this is to include backend dir in sys.path so that we can import from db,main.py

from db.base import Base
from db.session import get_db
from db.models.user import User
from db.models.session import Session
from apis.base import api_router
from schemas.session import CreateSession
from schemas.user import UserCreate


def start_application():
    app = FastAPI()
    app.include_router(api_router)
    return app


SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# Use connect_args parameter only with sqlite
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    """
    Create a fresh database on each test case.
    """
    Base.metadata.create_all(engine)  # Create the tables.
    _app = start_application()
    yield _app
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session  # use the session in tests.
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(
    app: FastAPI, db_session: SessionTesting
) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client


#making own fixture
@pytest.fixture
def test_user(db_session):
    #Creating a new user
    user = User(id=1,email="test@email.com", password="test_password")  
    db_session.add(user)
    db_session.commit()
   
    yield user
   
    #After the test runs, cleaning up the database
    db_session.delete(user)
    #committing
    db_session.commit()
 

 #making own fixture
@pytest.fixture
def test_sessions(db_session,test_user):
    #Creating a new session
    user_session = Session(user_id=test_user.id)
    db_session.add(user_session)
    db_session.commit()
   
    yield user_session  
   
    #After the test runs, cleaning up the database
    db_session.delete(user_session)
    db_session.commit()        