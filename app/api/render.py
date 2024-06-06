from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.schemas.student import StudentSchema
from app.api.student import get_students
from app.api.lesson import get_lessons

from fastapi import APIRouter, Depends
from app.schemas.lesson import LessonCreateSchema, LessonSchema
from app.models import Lesson
from sqlalchemy.orm import Session
from app.database.postreges import get_db

router = APIRouter(tags=["Render"])

t = Jinja2Templates("app/templates")


@router.get("/", response_class=HTMLResponse)
def home(
    request: Request,
    students: list[StudentSchema] = Depends(get_students),
    lessons: list[Lesson] = Depends(get_lessons),
):
    return t.TemplateResponse(
        request=request,
        name="index.html",
        context={"students": students, "lessons": lessons},
    )
