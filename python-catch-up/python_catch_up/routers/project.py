import json
from fastapi import APIRouter, Query, Response

from schemas.schemas import ProjectPydantic, ProjectPydanticInput
from services import project_crud

router = APIRouter()


@router.get("/projects", response_model=list[ProjectPydantic])
async def get_projects(response: Response,
                    sort: str = Query('["id","ASC"]'),
                    range: str = Query('[0,9]'),
                    filter: str = Query("{}")):
        
    projects: list[ProjectPydantic] = [] # type: ignore
    # getManyの処理
    if 'ids' in filter:
        filter_dict = json.loads(filter)
        projects = await project_crud.get_project_in_bulk(ids=filter_dict["ids"])
    else:
    # getListの処理
        start, end = json.loads(range)
        filter_dict = json.loads(filter)
        sort_value, type = json.loads(sort)
        if type != "ASC":
            sort_value = f"-{sort_value}"
        total = await project_crud.get_projects_count(filter=filter_dict)
        response.headers['Content-Range'] = f'projects {start}-{end}/{total}'
        projects = await project_crud.get_projects(order_by=sort_value, rangeStart=int(start), rangeEnd=int(end), filter=filter_dict)
    return projects

@router.get("/projects/{project_id}", response_model=ProjectPydantic)
async def get_project(project_id: int):
    client = await project_crud.get_project(id=project_id)
    return client

@router.post("/projects", response_model=ProjectPydantic)
async def create_project(project_input: ProjectPydanticInput): # type: ignore
    client = await project_crud.create_project(project_input=project_input)
    return client

@router.put("/projects/{project_id}", response_model=ProjectPydantic)
async def update_project(project_id: int, project_input: ProjectPydanticInput): # type: ignore
    client = await project_crud.update_project(id=project_id, project_input=project_input)
    return client


@router.delete("/projects/{project_id}", response_model=ProjectPydantic)
async def delete_project(project_id: int):
    client = await project_crud.delete_project(id=project_id)
    return client

@router.delete("/projects", response_model=list[ProjectPydantic])
async def delete_many_project(filter: str = Query("{}")):
    filter_dict = json.loads(filter)
    client = await project_crud.delete_many_project(ids=filter_dict["id"])
    return client
