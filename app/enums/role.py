from enum import Enum


class Role(str, Enum):
    GUEST = "GUEST"
    ADMIN = "ADMIN"
    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
