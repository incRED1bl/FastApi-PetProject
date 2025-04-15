from models.users import User
from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas.users.request import UserUpdate, UserCreate
from fastapi.exceptions import HTTPException
from dao.user import UserDAO


def create_user(data: UserCreate, sess: Session) -> User:
    return UserDAO.create(User(name=data.name), sess)

def get_user(id: int, sess: Session) -> User | None:
    return UserDAO.get(id, sess)

def update(data: UserUpdate, id: int, sess: Session) -> User:
    return UserDAO.update(id, {"name": data.name}, sess)

def delete_user(id: int, sess: Session):
    user = UserDAO.get(id, sess)
    if not user:
        raise HTTPException(204, detail="User not found")
    return UserDAO.delete(id, sess)
