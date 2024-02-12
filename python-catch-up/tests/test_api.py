import pytest


@pytest.mark.asyncio
async def test_create_programmer(client):
    json = {
        "name": "一郎",
        "technologies": ["Swift"] 
    }
    response = await client.post(url="/programmers/create", json=json)
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "name": "一郎",
        "technologies": [
            {
                "id": 1,
                "name": "Swift"
            }
        ]
    }

@pytest.mark.asyncio
async def test_get_programmers(client):
    response = await client.get(url="/programmers/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "name": "一郎",
            "technologies": [
                {
                    "id": 1,
                    "name": "Swift"
                }
            ]
        }
    ]

@pytest.mark.asyncio
async def test_get_programmer(client):
    response = await client.get(url="/programmers/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "一郎",
        "technologies": [
            {
                "id": 1,
                "name": "Swift"
            }
        ]
    }
    response = await client.get(url="/programmers/999")
    assert response.status_code == 404
    assert response.json() == {
        "code": 404,
        "title": "ユーザが存在しません",
        "message": "画面を更新して、再度やり直してください"
    }
    
@pytest.mark.asyncio
async def test_update_programmer(client):
    json = {
        "name": "新一郎",
        "technologies": ["Swift", "Flutter"] 
    }
    response = await client.put(url="/programmers/1", json=json)
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "新一郎",
        "technologies": [
            {
                "id": 1,
                "name": "Swift"
            },
            {
                "id": 2,
                "name": "Flutter"
            }
        ]
    }
    response = await client.put(url="/programmers/999", json=json)
    assert response.status_code == 404
    assert response.json() == {
        "code": 404,
        "title": "ユーザが存在しません",
        "message": "画面を更新して、再度やり直してください"
    }

@pytest.mark.asyncio
async def test_delete_programmer(client):
    response = await client.delete(url="/programmers/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "新一郎",
        "technologies": [
            {
                "id": 1,
                "name": "Swift"
            },
            {
                "id": 2,
                "name": "Flutter"
            }
        ]
    }
    response = await client.delete(url="/programmers/999")
    assert response.status_code == 404
    assert response.json() == {
        "code": 404,
        "title": "ユーザが存在しません",
        "message": "画面を更新して、再度やり直してください"
    }
