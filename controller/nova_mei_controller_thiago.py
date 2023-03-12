from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlmodel import Session, select

from db.database import engine
from models.model import Nova_mei, Ocupacao, RelacaoOcupacaoXNovaMEI


# def allMei():
#     with Session(engine) as session:
#         statement = select(Nova_mei)
    
#         results = session.exec(statement).all()
#         return results

def createMei(novaMei: Nova_mei):
    with Session(engine) as session:
        existing_mei = session.query(Nova_mei).filter(Nova_mei.cpf == nova_mei.cpf).first()
        if existing_mei:
            return {
                "message": f"Já existe uma solicitação com o CPF {novaMei.cpf} em andamento."
            }
        nova_mei = Nova_mei(
                            id=None,
                            cpf=novaMei.cpf,
                            objetivo_viabilidade=novaMei.objetivo_viabilidade,
                            inscricao_endereco=novaMei.inscricao_endereco,
                            tipo_endereco=novaMei.tipo_endereco,
                            endereco=novaMei.endereco,
                            nr_endereco=novaMei.nr_endereco
        )
        session.add(nova_mei)
        session.commit()
        session.refresh(nova_mei)
        
        print(nova_mei)
        
        for i in range(3):
            cnae = RelacaoOcupacaoXNovaMEI(
                nova_mei_id=nova_mei.id,
                ocupacao_id=int(input("ID da ocupacao: ")),
                is_primario=False
            )
            session.add(cnae)
            session.commit()

# def createUser(user: User):
#     with Session(engine) as session:
#         existing_user = session.query(User).filter(User.name == user.name).first()
#         if existing_user:
#             return {
#                 "Message": f"Usuario com nome {user.name} já existe."
#                 }
#         new_user = User(id=None, 
#                         name=user.name,
#                         email=user.email,
#                         phone=user.phone,
#                         whatsapp=user.whatsapp,
#                         password=user.password,
#                         address=user.address
#                         )
#         session.add(new_user)
#         session.commit()
#         session.refresh(new_user)
#         return new_user


# def findUser(id):
#     with Session(engine) as session:
#         statement = select(User).where(User.id == id)

#         results = session.exec(statement).first()
#         print(results)
#         return results


# def editUser(userID, user: User):
#     with Session(engine) as session:
#         statement = select(User).where(User.id == userID)
#         results = session.exec(statement).first()
#         results.name = user.name
#         results.email = user.email
#         results.phone = user.phone
#         results.whatsapp = user.whatsapp
#         results.password = user.password
#         results.address = user.address

#         session.add(results)
#         session.commit()
#         session.refresh(results)
#         print(results)
#         return JSONResponse(content=jsonable_encoder(results))


# def deleteUser(userID):
#     with Session(engine) as session:
#         statement = select(User).where(User.id == userID)
#         results = session.exec(statement).first()
#         session.delete(results)
#         session.commit()
#         print(f"Apagou o usuario com ID {userID}")
#         return True


# cadastrarUser()
# buscaUser(1)
# editUser(1)
# deleteUser(1)
