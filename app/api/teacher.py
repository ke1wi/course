from fastapi import APIRouter, Depends, HTTPException
from app.schemas.teacher import TeacherCreateSchema, TeacherSchema
from app.models import Teacher
from sqlalchemy.orm import Session
from app.database.postreges import get_db


router = APIRouter(prefix="/teacher", tags=["Teacher"])


@router.post("/", response_model=TeacherSchema)
def create_teacher(teacher_create: TeacherCreateSchema, db: Session = Depends(get_db)):
    new_teacher = Teacher(**teacher_create.model_dump())
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher


@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    db.delete(teacher)
    db.commit()
    return {"message": "Teacher deleted successfully"}
