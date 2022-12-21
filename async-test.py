import pytest
from httpx import AsyncClient
from asyncmain import app


@pytest.mark.anyio
async def test_main():
    data ={
        'output': 'Hello World'
    }
    client: AsyncClient
    async with AsyncClient(app=app,base_url='http://127.0.0.1:8000') as client:
        response = await client.get('/records')
    assert response.status_code == 404
    #assert  response.json() == data


