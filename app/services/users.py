from models.users import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from schemas.users.request import UserUpdate, UserCreate
from fastapi.exceptions import HTTPException
from dao.user import UserDAO


async def create_user(data: UserCreate, sess: AsyncSession) -> User:
    return await UserDAO.create(User(name=data.name), sess)

async def get_user(id: int, sess: AsyncSession) -> User | None:
    return await UserDAO.get(id, sess)

async def update(data: UserUpdate, id: int, sess: AsyncSession) -> User:
    return await UserDAO.update(id, {"name": data.name}, sess)

async def delete_user(id: int, sess: AsyncSession):
    user = await UserDAO.get(id, sess)
    if not user:
        raise HTTPException(204, detail="User not found")
    return UserDAO.delete(id, sess)
