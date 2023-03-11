from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import SessionLocal
from models.model_hipizza import User

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post('/login')
def login(email: str, senha: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email, User.password == senha).first()
    if user:
        return {"message": "Login successful"}
    else:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"message": "Invalid login credentials"})
