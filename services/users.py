from Training.models.users import User
from sqlalchemy.orm import Session
from Training.dto.users import User as UserDto

def create_user(data: UserDto, db: Session):
    user = User(name=data.name)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        db.rollback()
        raise Exception(f"Error creating user: {e}")
    return user

def get_user(id: int, db: Session):
    return db.query(User).filter(User.id == id).first()

def update(data: UserDto, id: int, db: Session):
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
