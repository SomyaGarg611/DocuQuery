#testing the create session api functionality
def test_create_session(client):
    data = {"user_id" : 1}
    response = client.post("/create-session" , json=data)
    assert response.status_code==201
    assert response.json()["user_id"]==1


import pytest
# from sqlalchemy.orm import Session
# from db.models.session import Session

#testing the fetch sessions api functionality
def test_fetch_sessions(client, test_user, test_sessions):
    response = client.get(f"/fetch-sessions/{test_user.id}")
    assert response.status_code == 200  
    sessions_data = response.json()
    assert isinstance(sessions_data, list)  
    assert len(sessions_data) > 0