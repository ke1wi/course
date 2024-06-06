from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import logging
from app.api import routers


app = FastAPI()
app.mount(
    "/static",
    StaticFiles(
        directory="app/static",
    ),
    name="static",
)


for router in routers:
    app.include_router(router)


logging.basicConfig(level="DEBUG")
