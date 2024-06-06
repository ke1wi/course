from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from app.models import Journal
from sqlalchemy.orm import Session
from app.database.postreges import get_db
from datetime import date as d
from app.models import User
from app.schemas.user import UserCreateSchema
from app.auth.auth import get_password_hash, create_access_token, verify_password

router = APIRouter(prefix="/user", tags=["User"])
t = Jinja2Templates("app/templates")


@router.post("/user/signup")
def signup_user(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    db_user = db.query(User).filter(User.email == email).first()

    if db_user:
        return t.TemplateResponse(
            request=request,
            name="registration.html",
            context={"message": "Користувач з такою поштою вже існує!"},
        )

    user = UserCreateSchema(
        name=name, email=email, hashed_password=get_password_hash(password)
    )
    success = db.add(User(**user.model_dump()))

    token = create_access_token(email)

    return JSONResponse(
        status_code=201,
        content={"message": "Користувач створений успішно!", "token": token},
    )


@router.post("/user/signin")
def signin_user(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        return JSONResponse(
            status_code=400,
            content={"message": "Користувача з такою поштою не існує!"},
        )

    if verify_password(get_password_hash(password), db_user.hashed_password):
        token = create_access_token(email)
        return JSONResponse(
            status_code=200, content={"message": "Успішний вхід", "token": token}
        )

    return JSONResponse(status_code=400, content={"message": "Неправильний пароль!"})
