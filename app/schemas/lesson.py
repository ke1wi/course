from .base import Base


class LessonSchema(Base):
    id: int
    name: str


class LessonCreateSchema(Base):
    name: str
