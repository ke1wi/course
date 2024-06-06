from fastapi import APIRouter, Depends, HTTPException
from app.schemas.student import StudentCreateSchema, StudentSchema
from app.models import Student
from sqlalchemy.orm import Session
from app.database.postreges import get_db

router = APIRouter(prefix="/student", tags=["Student"])


@router.get("/")
def get_students(db: Session = Depends(get_db)) -> list[StudentSchema]:
    students = db.query(Student).all()
    return [{"id": student.id, "name": student.name} for student in students]


@router.post("/", response_model=StudentSchema)
def create_student(student_create: StudentCreateSchema, db: Session = Depends(get_db)):
    new_student = Student(**student_create.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}
