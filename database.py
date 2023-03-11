from sqlmodel import SQLModel, create_engine
from sqlalchemy.orm import sessionmaker
import models.model_hipizza

engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
