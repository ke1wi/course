from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Journal(Base):
    __tablename__ = "journal"

    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lesson.id"))
    student_id = Column(Integer, ForeignKey("student.id"))
    mark = Column(Integer)
    date = Column(Date)


class Lesson(Base):
    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey("teacher.id"))


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Teacher(Base):
    __tablename__ = "teacher"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
