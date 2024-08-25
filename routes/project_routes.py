from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from app.db import (
    add_project,
    delete_project,
    update_project,
    retrieve_project,
    get_project_list
)
from auth.auth_bearer import JWTBearer
from models.models import (
    ResponseModel,
    ErrorResponseModel,
    ProjectSchema,
    UpdateProjectModel
)

router = APIRouter()

# Create project
@router.post("/", dependencies=[Depends(JWTBearer())], response_description="Project data added into the database")
async def add_project_data(project: ProjectSchema = Body(...)):
    project = jsonable_encoder(project)
    new_project = await add_project(project)
    return ResponseModel(new_project, "Project added successfully.")

# Get list of projects
@router.get("/", response_description="Project retrieved")
async def get_projectList():
    projects = await get_project_list()
    if projects:
        return ResponseModel(projects, "Project data retrieved successfully")
    return ResponseModel(projects, "Empty list returned")

# Get project by ID
@router.get("/{id}", response_description="Project data retrieved")
async def get_projectList_data(id: str):
    project = await retrieve_project(id)
    if project:
        return ResponseModel(project, "Project data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Project doesn't exist.")

# Update project
@router.put("/{id}", dependencies=[Depends(JWTBearer())])
async def update_project_data(id: str, req: UpdateProjectModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_list = await update_project(id, req)
    if updated_list:
        return ResponseModel(
            f"Project with ID: {id} update is successful",
            "Project updated successfully",
        )
    return ErrorResponseModel("An error occurred", 404, "There was an error updating the data.")

# Delete project
@router.delete("/{id}", dependencies=[Depends(JWTBearer())], response_description="Project data deleted from the database")
async def delete_data(id: str):
    deleted_list = await delete_project(id)
    if deleted_list:
        return ResponseModel(
            f"Project with ID: {id} removed", "Project deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, f"Project with id {id} doesn't exist"
    )
