from .base import Base
from datetime import date


class MarkRequest(Base):

    student_id: int
    lesson_id: int
    mark: int
    date: date
