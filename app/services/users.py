from models.users import User
from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas.users.request import UserBase, UserCreate

def create_user(data: UserCreate, db: Session):
    user = User(name=data.name)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        db.rollback()
        raise Exception(f"Error creating user: {e}")
    return user

def get_user(id: int, sess: Session) -> User | None:
    return sess.execute(select(User).where(User.id == id)).scalar_one_or_none()

def update(data: UserBase, id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        return None
    user.name = data.name
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        db.rollback()
        raise Exception(f"Error updating user: {e}")
    return user

def delete_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        return None
    try:
        db.delete(user)
        db.commit()
    except Exception as e:
        db.rollback()
        raise Exception(f"Error deleting user: {e}")
    return {"message": "User deleted successfully"}
