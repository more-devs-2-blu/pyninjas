from fastapi import APIRouter
from main import app

from api.v1.endpoints import mei_routes

app.include_router(mei_routes.router)
