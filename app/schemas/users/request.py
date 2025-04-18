from app.schemas.cfg import BaseConfig

class UserBase(BaseConfig):
    id: int
    name: str


class UserCreate(BaseConfig):
    name: str


class UserUpdate(BaseConfig):
    name: str
