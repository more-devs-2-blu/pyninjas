import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from sqlmodel import SQLModel, create_engine
from sqlalchemy.orm import sessionmaker
from models import model

engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
