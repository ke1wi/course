from fastapi import Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.schemas.student import StudentSchema
from app.api.student import get_students
from app.api.lesson import get_lessons
from app.models import Journal, Student

from fastapi import APIRouter, Path
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


@router.get("/rates/{student_id}", response_class=HTMLResponse)
async def rates(
    request: Request,
    student_id: int = Path(...),
    db: Session = Depends(get_db),
):
    student = db.query(Student).filter(Student.id == student_id).first()
    journal = db.query(Journal).filter(Journal.student_id == student_id).all()
    return t.TemplateResponse(
        request=request,
        name="journal.html",
        context={"student": student, "journal": journal},
    )
