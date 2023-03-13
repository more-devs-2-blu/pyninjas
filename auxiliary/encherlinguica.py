import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from db.database import engine
from sqlmodel import Session, select
# from models.model import ClassRoom, Student, Group
from sqlalchemy.orm import selectinload
from models.model import Nova_mei, Ocupacao, RelacaoOcupacaoXNovaMEI

import random

# def cadastraClass():
#     with Session(engine) as session:
#         new_class = ClassRoom(id=None, name=input("Nome da Classe: "))
#         session.add(new_class)
#         session.commit()
#         #session.refresh(new_class)
#         print(new_class)

def cadastrarNovaMei():
    with Session(engine) as session:
        nova_mei = Nova_mei(
            # id=None,
            cpf="12343",
            objetivo_viabilidade="asdasd",
            inscricao_endereco="asd",
            tipo_endereco="Tipo de Endereço:",
            endereco="Digite o seu endereço: ",
            nr_endereco="Nr Endereço: "
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
        

def cadastrarOcupacao(): 
    with Session(engine) as session:
        new_ocupacao = Ocupacao(
                id=None,
                descricao=input("Descricao: "),
                cnae=input("CNAE:")
        )
        session.add(new_ocupacao)
        session.commit()
        print(new_ocupacao)

def cadastrarUser():
    with Session(engine) as session:
        new_user = User(id=None, name=input("Nome: "),
                        email=input("Email: "),
                        phone=input("Telefone: "),
                        password=input("Senha: "),
                        address=input("Endereço: ")   
                        )
        session.add(new_user)
        session.commit()
        #session.refresh(new_user)
        print(new_user)

def cadastrarItem():
    with Session(engine) as session:
        new_item = Item(id=None, name=input("Nome: "),
                        price=input("Preço: "),
                        description=input("Descrição: ") 
                        )
        session.add(new_item)
        session.commit()
        #session.refresh(new_item)
        print(new_item)

def buscaUser(id):
    with Session(engine) as session:
        statement = select(User).where(User.id==id)
        
        results = session.exec(statement).first()
        print(results)
        return results
    
def buscaItem(id):
    with Session(engine) as session:
        statement = select(Item).where(Item.id==id)
        
        results = session.exec(statement).first()
        print(results)
        return results

def editUser(userID):
    with Session(engine) as session:
        statement = select(User).where(User.id == userID)
        results = session.exec(statement).first()
        
        # if not results:
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        #         detail = {"message": f"No Student found with id {userID}"}
        #     )
        # else:
        results.name = input("Novo Nome: ")

        session.add(results)
        session.commit()
        session.refresh(results)
        print(results)
            # return JSONResponse(content=jsonable_encoder(results))
        
def deleteUser(userID):
    with Session(engine) as session:
        statement = select(User).where(User.id == userID)
        results = session.exec(statement).first()
        # if not results:
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        #         detail = {"message": f"No Student found with id: {userID}"}
        #     )
        # else:
        session.delete(results)
        session.commit()
        print(f"Apagou o usuario com ID {userID}")
            #Não sei exatamente o que retornar aqui
        return True

# def cadastrarGrupo(idClassRoom):
#     with Session(engine) as session:
#         new_class = Group(id=None, name=input("Nome do grupo: "), description=input("Descrição do grupo: "), id_classroom=idClassRoom)
#         session.add(new_class)
#         session.commit()
#         #session.refresh(new_class)
#         print(new_class)
        
# def buscaClasseAlunos():
#     with Session(engine) as session:
#         statement = select(ClassRoom).options(selectinload(ClassRoom.students)).options(selectinload(ClassRoom.groups))
        
#         results = session.exec(statement).all()
#         print(results)
#         return results
    
# #TEste!!! altamente errado!
# def enfiaAlunoNoGrupo(id_student, id_classe):
#     with Session(engine) as session:
#         statement1 = select(Student).where(Student.id == id_student)
#         statement2 = select(Group).where(Group.id_classroom == id_classe)
#         estudante = session.exec(statement1).first()
#         grupos = session.exec(statement2).all()
#         random.shuffle(grupos)
#         estudante.id_group = grupos[0].id
#         estudante.group = grupos[0]
#         print("Primeiro grupo: "+str(grupos[0]))
#         print ("Estudante: "+str(estudante))
#         print("Grupos: "+str(grupos))
#         session.add(estudante)
#         session.commit()
#         session.refresh(estudante)
#         return estudante
        

# def buscaGrupo():
#     with Session(engine) as session:
#         statement = select(Group).options(selectinload(Group.students))
        
#         results = session.exec(statement).all()
#         print(results)
#         return results

## Criando order functions

from datetime import datetime

def todasOrders():
    with Session(engine) as session:
        statement = select(Order)

        results = session.exec(statement).all()
        print(results)
        return results

# Na controlar adicionar o parametro "order:Order" pra adicionar os valores
def criaOrder(userID, itemID):
    with Session(engine) as session:
        new_order = Order(id=None, 
                          status=input('Status: '),
                          shipping_value=input('Frete: '),
                          payment_method=input('Metodo Pagto: '),
                          order_date=datetime.today(),
                          total_price=input('Total: '),
                          user_id=userID,
                          item_id=itemID)
        session.add(new_order)
        session.commit()
        return new_order
    
def buscaOrder(orderID: int = None):
    with Session(engine) as session:
        statement = select(Order).where(Order.id == orderID)

        results = session.exec(statement).first()
        print(results)
        return results
    
# Na controlar adicionar o parametro "order:Order" pra adicionar os valores
def editarOrder(orderID, order:Order = None):
    with Session(engine) as session:
        statement = select(Order).where(Order.id == orderID)
        results = session.exec(statement).first()
        results.status = input('Status: ')
        results.shipping_value = input('Frete: ')
        results.payment_method = input('Pagto: ')
        results.total_price = input('Total: ')
        results.user_id = input(f'Deseja Alterar? ID Atual {results.user_id} : ')
        results.item_id = input(f'Deseja Alterar? ID Atual {results.item_id} : ')

        session.add(results)
        session.commit()
        session.refresh(results)
        print(results)
        return results

def deletarOrder(orderID):
    with Session(engine) as session:
        statement = select(Order).where(Order.id == orderID)
        results = session.exec(statement).first()
        session.delete(results)
        session.commit()
        print(f"Order com id {orderID} deletada com sucesso")
        return True

# Testando relacionamento entre tabelas buscando infos pelos IDs (FK)
# e retornando o valor "name" como no exemplo abaixo

def testeBuscaOrder(orderID):
    with Session(engine) as session:
        # Nao consegui fazer esse teste usando um statement só, deve haver uma maneira.
        statement = select(Order, User).join(User).where(Order.id == orderID)
        statement2 = select(Order, Item).join(Item).where(Order.id == orderID)

        result = session.exec(statement).one()
        result2 = session.exec(statement2).one()
        user_id = result.User.name
        item_id = result2.Item.name
        
        print(user_id)
        print(item_id)


def buscaNovaMEI(id):
    with Session(engine) as session:
        statement = select(Nova_mei).where(Nova_mei.id==id)
        
        results = session.exec(statement).first()
        
        statement_cnaes = select(RelacaoOcupacaoXNovaMEI).where(RelacaoOcupacaoXNovaMEI.nova_mei_id == id)
        results_cnaes = session.exec(statement_cnaes).all()
        
        print("MEI:\n ", results)
        print("\nCNAES: ", results_cnaes)
        return results



# while True:
#     print("Escolha uma das opções: ")
#     print("\n 1 - Cadastrar Classe\n 2 - Cadastrar aluno\n 3 - Cadastrar Grupo\n 4 - Listar tudo\n Digite qualquer outro número para sair.\n")
#     match input(" > "):
#         case "1":
#             cadastraClass()
#         case "2":
#             cadastrarStudent(input("Informe o ID da sala: "))
#         case "3":
#             cadastrarGrupo(input("Informe o ID da sala: "))
#         case "4":
#             buscaClasseAlunos()
#         case _:
#             break

# cadastrarOcupacao()
# cadastrarNovaMei()

buscaNovaMEI(5)


# def teste(v1 = 'Thiago'):
#     print(v1)

# todasOrders()
# criaOrder(3, 2)
# buscaOrder(1)
# testeBuscaOrder(3)
# editarOrder(1)
# deletarOrder(5)


# enfiaAlunoNoGrupo(1,1)
# cadastrarUser()
# cadastrarItem()
# buscaUser(1)
# buscaItem(2)

# editUser(1)
# deleteUser(1)
# teste('Jean')
#buscaGrupo()