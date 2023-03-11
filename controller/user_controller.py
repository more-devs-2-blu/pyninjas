from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlmodel import Session, select

from database import engine
from models.model_hipizza import User


def allUsers():
    with Session(engine) as session:
        statement = select(User)
    
        results = session.exec(statement).all()
        return results


def createUser(user: User):
    with Session(engine) as session:
        existing_user = session.query(User).filter(User.name == user.name).first()
        if existing_user:
            return {
                "Message": f"Usuario com nome {user.name} já existe."
                }
        new_user = User(id=None, 
                        name=user.name,
                        email=user.email,
                        phone=user.phone,
                        whatsapp=user.whatsapp,
                        password=user.password,
                        address=user.address
                        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user


def findUser(id):
    with Session(engine) as session:
        statement = select(User).where(User.id == id)

        results = session.exec(statement).first()
        print(results)
        return results


def editUser(userID, user: User):
    with Session(engine) as session:
        statement = select(User).where(User.id == userID)
        results = session.exec(statement).first()
        results.name = user.name
        results.email = user.email
        results.phone = user.phone
        results.whatsapp = user.whatsapp
        results.password = user.password
        results.address = user.address

        session.add(results)
        session.commit()
        session.refresh(results)
        print(results)
        return JSONResponse(content=jsonable_encoder(results))


def deleteUser(userID):
    with Session(engine) as session:
        statement = select(User).where(User.id == userID)
        results = session.exec(statement).first()
        session.delete(results)
        session.commit()
        print(f"Apagou o usuario com ID {userID}")
        return True


# cadastrarUser()
# buscaUser(1)
# editUser(1)
# deleteUser(1)
