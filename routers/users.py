from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Training.database import get_db
from Training.services.users import create_user, get_user, update, delete_user
from Training.dto.users import User as UserDto

router = APIRouter()

@router.post("/", tags=["users"])
async def create(data: UserDto, db: Session = Depends(get_db)):
    return create_user(data, db)

@router.get("/{id}", tags=["users"])
async def get(id: int, db: Session = Depends(get_db)):
    user = get_user(id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{id}", tags=["users"])
async def update_user(id: int, data: UserDto, db: Session = Depends(get_db)):
    user = update(data, id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{id}", tags=["users"])
async def delete(id: int, db: Session = Depends(get_db)):
    user = delete_user(id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
