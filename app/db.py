import motor.motor_asyncio
from dotenv import load_dotenv
from bson.objectid import ObjectId
import os
import bcrypt
from datetime import datetime

load_dotenv()

MONGO_DETAILS = os.getenv('MONGO_URI')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

projectDB = client.project
userDB = client.user

project_collection = projectDB.get_collection("project_collection")
user_collection = userDB.get_collection("user_collection")

def project_parser(project) -> dict:
    return {
        "id": str(project["_id"]),  # Unique identifier
        "task": project["task"],
        "createdBy": project["createdBy"],
        "startDate": project["startDate"],
        "endDate": project["endDate"]
    }

async def get_project_list():
    projectList = []
    async for project in project_collection.find():
        temp = project_parser(project)
        projectList.append(temp)
    return projectList

async def add_project(project_data: dict) -> dict:
    project = await project_collection.insert_one(project_data)
    new_project = await project_collection.find_one({"_id": project.inserted_id})
    return project_parser(new_project)

async def retrieve_project(id: str) -> dict:
    project = await project_collection.find_one({"_id": ObjectId(id)})
    if project:
        return project_parser(project)

async def update_project(id: str, data: dict):
    if len(data) < 1:
        return False
    project = await project_collection.find_one({"_id": ObjectId(id)})
    if project:
        updated_project = await project_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        return updated_project.modified_count > 0
    return False

async def delete_project(id: str):
    project = await project_collection.find_one({"_id": ObjectId(id)})
    if project:
        await project_collection.delete_one({"_id": ObjectId(id)})
        return True

async def get_user(email: str, password: str):
    user = await user_collection.find_one({"email": email})
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return True
    return False
