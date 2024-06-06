from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from fastapi import Depends, Request
from fastapi.exceptions import HTTPException
from app.settings import settings
from datetime import datetime, timedelta, UTC
from app.models import User
from app.database.postreges import get_db
from sqlalchemy.orm import Session

ACCESS_TOKEN_EXPIRE_MINUTES = 3000

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
COOKIE_NAME = "Authorization"

# create Token


def create_access_token(user_email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_email).first()
    expiration_time = datetime.now(UTC) + timedelta(weeks=2)
    payload = {
        "user_id": user.id,
        "email": user.email,
        "name": user.name,
        "hashed_password": user.hashed_password,
    }
    token_payload = {**payload, "exp": expiration_time}
    return jwt.encode(
        token_payload,
        key=settings.JWT_SECRET.get_secret_value(),
        algorithm=settings.ALGORITHM.get_secret_value(),
    )


def verify_token(token):
    try:
        payload = jwt.decode(token, key=settings.JWT_SECRET.get_secret_value())
        user_id = payload.get("user_id")
        return user_id
    except Exception as ex:
        raise ex


# password hash


def get_password_hash(password: str):
    return pwd_context.hash(password)


# password verify


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_current_user_from_token(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    user_id = verify_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


def get_current_user_from_cookie(request: Request) -> User:
    token = request.cookies.get(COOKIE_NAME)
    if token:
        user = verify_token(token)
        return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    return token


