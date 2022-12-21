try:
    from fastapi.testclient import TestClient
    from main import app
    import pytest
except:
    print('Error Importing Libraries')

client = TestClient(app)


def test_retrieve_data():
    response = client.get('/records/')
    assert response.status_code == 200


def test_retrieve_specific_data():
    response = client.get('/record/1')
    assert response.status_code == 200


def test_retrieve_specificData_fail():
    response = client.get('/record/10000000')
    data = {
        "detail": "Item not found"
    }
    assert response.status_code == 404
    assert response.json() == data
