from .database import Base
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Type, TypeVar, Generic

from sqlalchemy import select, delete, update


T = TypeVar("T", bound=Base)


class TemplateDAO(Generic[T]):
    def __init__(self, db_model: T) -> None:
        self.db_model: T = db_model

    def get(self, id: int, sess: Session) -> T | None:
        stmt = select(self.db_model).where(self.db_model.id == id)
        return sess.execute(stmt).scalar_one_or_none()

    def get_scalar(self, id: int, sess: Session) -> T:
        stmt = select(self.db_model).where(self.db_model.id == id)
        return sess.execute(stmt).scalar_one()

    def delete(self, id: int, sess: Session) -> None:
        stmt = self.db_model.__table__.delete().where(self.db_model.id == id)
        sess.execute(stmt)

    def update(self, id: int, values: dict, sess: Session) -> T:
        stmt = (
            self.db_model.__table__.update()
            .where(self.db_model.id == id)
            .values(**values)
        )
        sess.execute(stmt)
        return self.get_scalar(id, sess)

    def create(self, instance: T, sess: Session) -> T:
        sess.add(instance)
        sess.flush()
        return instance

    def create_all(self, instances: list[T], sess: Session) -> list[T]:
        sess.add_all(instances)
        sess.flush()
        return instances


def construct_dao(db_model: Type[T]) -> Type[TemplateDAO[T]]:
    class CustomDAO(TemplateDAO[T]):
        def __init__(self, db_model: T) -> None:
            super(CustomDAO, self).__init__(db_model)

    return CustomDAO
