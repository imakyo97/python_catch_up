import json
from fastapi import APIRouter, Query, Response

from schemas.schemas import ClientPydantic, ClientPydanticData
from services import client_crud

router = APIRouter()


@router.get("/clients", response_model=list[ClientPydantic])
async def get_clients(response: Response,
                    sort: str = Query('["id","ASC"]'),
                    range: str = Query('[0,9]'),
                    filter: str = Query("{}")):
        
    clients: list[ClientPydantic] = [] # type: ignore
    # getManyの処理
    if 'ids' in filter:
        filter_dict = json.loads(filter)
        clients = await client_crud.get_client_in_bulk(ids=filter_dict["ids"])
    else:
    # getListの処理
        start, end = json.loads(range)
        filter_dict = json.loads(filter)
        sort_value, type = json.loads(sort)
        if type != "ASC":
            sort_value = f"-{sort_value}"
        total = await client_crud.get_clients_count(filter=filter_dict)
        response.headers['Content-Range'] = f'posts {start}-{end}/{total}'
        clients = await client_crud.get_clients(order_by=sort_value, rangeStart=int(start), rangeEnd=int(end), filter=filter_dict)
    return clients

@router.get("/clients/{client_id}", response_model=ClientPydantic)
async def get_client(client_id: int):
    client = await client_crud.get_client(id=client_id)
    return client

@router.post("/clients", response_model=ClientPydantic)
async def create_client(client_data: ClientPydanticData): # type: ignore
    client = await client_crud.create_client(client_data=client_data)
    return client

@router.put("/clients/{client_id}", response_model=ClientPydantic)
async def update_client(client_id: int, client_data: ClientPydanticData): # type: ignore
    client = await client_crud.update_client(id=client_id, client_data=client_data)
    return client


@router.delete("/clients/{client_id}", response_model=ClientPydantic)
async def delete_client(client_id: int):
    client = await client_crud.delete_client(id=client_id)
    return client

@router.delete("/clients", response_model=list[ClientPydantic])
async def delete_many_client(filter: str = Query("{}")):
    filter_dict = json.loads(filter)
    client = await client_crud.delete_many_client(ids=filter_dict["id"])
    return client