from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, Enum
from sqlalchemy.orm import DeclarativeBase, relationship
from app.enums.role import Role


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    role = Column(Enum(Role), nullable=False)


class Journal(Base):
    __tablename__ = "journals"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False)
    mark = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)

    student = relationship("Student", back_populates="journal_entries")
    lesson = relationship("Lesson", back_populates="journal_entries")


class Student(User):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    role = Column(Enum(Role), default=Role.STUDENT)
    journal_entries = relationship("Journal", back_populates="student")


class Lesson(Base):
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    journal_entries = relationship("Journal", back_populates="lesson")


class Teacher(User):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    role = Column(Enum(Role), default=Role.TEACHER)
