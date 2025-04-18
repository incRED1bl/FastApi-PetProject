import traceback
import uvicorn

from fastapi import FastAPI, APIRouter
from fastapi.requests import Request
from fastapi.responses import Response
from fastapi.responses import JSONResponse

from app.schemas.cfg import BaseResponse

from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.database import SessionLocal


app = FastAPI()

router = APIRouter()


from app.routers.users import router as UserRouter

api_version = "/v1"

routes = APIRouter(prefix="/api", redirect_slashes=False)

routes.include_router(UserRouter, prefix=f"{api_version}/users", tags=["users"])

app.include_router(routes)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    async with SessionLocal() as session:
        request.state.sess = session
        try:
            response = await call_next(request)
            await session.commit()
        except Exception as e:
            await session.rollback()
            error_response = BaseResponse(status=500, message=str(e))
            response = JSONResponse(content=error_response.model_dump())
        return response


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
