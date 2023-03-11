from fastapi import APIRouter
from main import app

from api.v1.endpoints import user_routes
from api.v1.endpoints import item_routes
from api.v1.endpoints import order_routes
from api.v1.endpoints import auth

app.include_router(user_routes.router)
app.include_router(item_routes.router)
app.include_router(order_routes.router)
app.include_router(auth.router)