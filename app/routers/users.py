from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession



from services import users as user_service
from schemas.users.request import UserBase, UserCreate
from schemas.users.response import UserResponse
from schemas.cfg import BaseResponse

from fastapi.requests import Request


router = APIRouter()

@router.post("/", tags=["users"])
async def create(data: UserCreate, request: Request) -> BaseResponse[UserResponse]:
    sess: AsyncSession = request.state.sess
    return BaseResponse(data=UserResponse.model_validate(await user_service.create_user(data, sess)))

@router.get("/{id}", tags=["users"])
async def get_user(id: int, request: Request) -> BaseResponse[UserResponse]:
    sess: AsyncSession = request.state.sess
    if user := await user_service.get_user(id, sess):
        return BaseResponse(data=UserResponse.model_validate(user))
    return BaseResponse(status=204, message="User not found", data=None)

@router.get("/{id}/name", tags=["users"])
async def get_user_name(id: int, request: Request) -> str:
    sess: AsyncSession = request.state.sess
    if user := await user_service.get_user(id, sess):
        return user.name
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.put("/{id}", tags=["users"], response_model=UserResponse)
async def update_user(id: int, data: UserBase, request: Request):
    sess: AsyncSession = request.state.sess
    if user := await user_service.update(data, id, sess):
        return UserResponse(**user.__dict__)
    else:
        raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{id}", tags=["users"])
async def delete(id: int, request: Request) -> BaseResponse:
    sess: AsyncSession = request.state.sess
    return BaseResponse(data=await user_service.delete_user(id, sess))
