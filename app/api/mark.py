from fastapi import APIRouter, Depends, Form
from app.schemas.mark import MarkRequest
from app.models import Journal
from sqlalchemy.orm import Session
from app.database.postreges import get_db
from datetime import datetime

router = APIRouter(prefix="/mark", tags=["Mark"])


@router.post("/")
def create_mark(
    mark_request: MarkRequest,
    db: Session = Depends(get_db),
):
    new_mark = Journal(
        student_id=mark_request.student_id,
        lesson_id=mark_request.lesson_id,
        mark=mark_request.mark,
        date=datetime.now(),
    )
    db.add(new_mark)
    db.commit()
    db.refresh(new_mark)
    return new_mark
