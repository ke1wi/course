from .lesson import router as lesson_router
from .student import router as student_router
from .teacher import router as teacher_router
from .journal import router as journal_router
from .mark import router as mark_router
from .render import router as render_router
from .user import router as user_router


routers = [
    lesson_router,
    journal_router,
    student_router,
    teacher_router,
    mark_router,
    render_router,
    user_router,
]
