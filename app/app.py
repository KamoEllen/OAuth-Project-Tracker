from fastapi import FastAPI, Depends
from routes.project_routes import router as projectRouter
from routes.user_routes import router as userRouter



app = FastAPI()

app.include_router(userRouter, tags=["user"], prefix="/user")
app.include_router(projectRouter, tags=["project"], prefix="/project")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this app!"}
