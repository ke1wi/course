from .base import Base


class TeacherSchema(Base):
    id: int
    name: str


class TeacherCreateSchema(Base):
    name: str
