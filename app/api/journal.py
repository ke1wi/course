from fastapi import APIRouter, Depends
from app.models import Journal
from sqlalchemy.orm import Session
from app.database.postreges import get_db

router = APIRouter(prefix="/journal", tags=["Journal"])


@router.get("/{student_id}")
def get_journal(student_id: int, db: Session = Depends(get_db)):
    journal_entries = db.query(Journal).filter(Journal.student_id == student_id).all()
    return journal_entries
