#testing the create_user api functionality
def test_create_user(client):
    data = {"email":"testing@example.com", "password":"supersecret"}
    response = client.post("/create-user" , json=data)
    assert response.status_code==201
    assert response.json()["email"]=="testing@example.com"
