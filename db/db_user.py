from fastapi import Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.hash import Hash
from db.models import User
from log import logger
from schema import UserBase


def create_user(request: UserBase, db: Session = Depends(get_db)):
    from routers.user import router

    user = User(
        username=request.username,
        password=Hash.bcrypt(request.password),
        email=request.email,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    logger.info(f'Endpoint url: {router.prefix}')
    return user

