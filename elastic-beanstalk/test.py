import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Web App with Python Flask!'

def test_upload(client):
    response1 = client.get('/upload')
    assert response1.status_code == 200
    assert b"Upload to S3" in response1.data
    assert b"Choose file to be uploaded" in response1.data