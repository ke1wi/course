from .base import Base


class StudentSchema(Base):
    id: int
    name: str


class StudentCreateSchema(Base):
    name: str
