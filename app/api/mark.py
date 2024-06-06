from fastapi import APIRouter, Depends, Form, Request
from app.models import Journal
from sqlalchemy.orm import Session
from app.database.postreges import get_db
from datetime import date as d

router = APIRouter(prefix="/mark", tags=["Mark"])


@router.post("/")
async def create_mark(
    request: Request,
    student_id: int = Form(...),
    lesson_id: int = Form(...),
    mark: int = Form(...),
    db: Session = Depends(get_db),
):
    data = await request.form()
    student_id = int(data.get("student_id"))
    lesson_id = int(data.get("lesson_id"))
    mark = int(data.get("mark"))
    date = d.today()

    new_mark = Journal(lesson_id=lesson_id, student_id=student_id, mark=mark, date=date)
    db.add(new_mark)
    db.commit()
    db.refresh(new_mark)
    return {"message": "Оцінка додана успішно", "mark": new_mark}
