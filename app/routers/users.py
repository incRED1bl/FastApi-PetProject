from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session



from database.database import get_db
from services.users import create_user, get_user, update, delete_user
from schemas.users.request import UserBase, UserCreate
from schemas.users.response import UserResponse
from schemas.cfg import BaseResponse


router = APIRouter()

@router.post("/", tags=["users"])
async def create(data: UserCreate, db: Session = Depends(get_db)) -> BaseResponse[UserResponse]:
    return BaseResponse(data=UserResponse.model_validate(create_user(data, db)))

@router.get("/{id}", tags=["users"])
async def get_user(id: int, db: Session = Depends(get_db)) -> BaseResponse[UserResponse]:
    if user := get_user(id, db):
        return BaseResponse(data=UserResponse.model_validate(user))
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.get("/{id}/name", tags=["users"])
async def get_user_name(id: int, db: Session = Depends(get_db)) -> str:
    if user := get_user(id, db):
        return user.name
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.put("/{id}", tags=["users"], response_model=UserResponse)
async def update_user(id: int, data: UserBase, db: Session = Depends(get_db)):
    if user := update(data, id, db):
        return UserResponse(**user.__dict__)
    else:
        raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{id}", tags=["users"])
async def delete(id: int, db: Session = Depends(get_db)) -> BaseResponse:
    if not delete_user(id, db):
        raise HTTPException(status_code=404, detail="User not found")
    return BaseResponse(message="User deleted successfully")
