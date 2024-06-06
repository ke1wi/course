from .base import Base
from app.enums.role import Role


class UserSchema(Base):
    id: int
    name: str
    email: str
    is_active: bool
    is_superuser: bool
    role: Role

class UserCreateSchema(Base):
    name: str
    email: str
    hashed_password: str
