import uvicorn
from fastapi import FastAPI
from Training.database import engine, Base
from Training.routers.users import router as UserRouter

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(UserRouter, prefix="/users", tags=["users"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, workers=4)
