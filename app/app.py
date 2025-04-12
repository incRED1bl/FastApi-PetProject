import uvicorn

from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()

router = APIRouter()


from routers.users import router as UserRouter

api_version = "/v1"

routes = APIRouter(prefix="/api", redirect_slashes=False)

routes.include_router(UserRouter, prefix=f"{api_version}/users", tags=["users"])

app.include_router(routes)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8069, reload=True)
