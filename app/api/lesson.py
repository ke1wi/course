from fastapi import APIRouter, Depends
from app.schemas.lesson import LessonCreateSchema, LessonSchema
from app.models import Lesson
from sqlalchemy.orm import Session
from app.database.postreges import get_db

router = APIRouter(prefix="/lesson", tags=["Lesson"])


@router.get("/")
def get_lessons(db: Session = Depends(get_db)) -> list[LessonSchema]:
    lessons = db.query(Lesson).all()
    return [{"id": lesson.id, "name": lesson.name} for lesson in lessons]


@router.post("/", response_model=LessonSchema)
def create_lesson(student_create: LessonCreateSchema, db: Session = Depends(get_db)):
    new_lesson = Lesson(**student_create.model_dump())
    db.add(new_lesson)
    db.commit()
    db.refresh(new_lesson)
    return new_lesson
