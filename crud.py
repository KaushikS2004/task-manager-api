from sqlalchemy.orm import Session
import models
from utils.hashing import hash_password, verify_password




def create_user(db: Session, username: str, password: str):
    user = models.User(
    username=username,
    password=hash_password(password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user




def authenticate_user(db: Session, username: str, password: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def create_task(db: Session, task):
    db_task = models.Task(
        title=task.title,
        description=task.description
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session):
    return db.query(models.Task).all()


def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def update_task(db: Session, task_id: int, task):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        return None
    if task.title:
        db_task.title = task.title
    if task.description:
        db_task.description = task.description
    if task.status:
        db_task.status = task.status
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        return None
    db.delete(db_task)
    db.commit()
    return db_task