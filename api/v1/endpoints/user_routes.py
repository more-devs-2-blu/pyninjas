from controller.user_controller import editUser, createUser, deleteUser, findUser, allUsers
from fastapi import APIRouter, Response
from fastapi import status
from models.model_hipizza import User

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix='/user',
    tags=['user']
)


# Busca/lista usuarios cadatrados
##
@router.get(
    '/',
    summary='Retorna uma lista de users',
    description='Retorna uma lista de todos os users cadastrados em formato JSON',
    response_description='Lista de users cadastrados.',
    status_code=status.HTTP_200_OK)
def busca_users(response: Response):
    lista_users = allUsers()
    if lista_users:
        response.status_code = status.HTTP_200_OK
        return JSONResponse(content=jsonable_encoder(lista_users))
    else:        
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND


# Busca de users por ID

@router.get(
    '/{id}',
    summary='Retorna um user com base no ID especificado',
    description='Retorna um user cadastrado em formato JSON',
    response_description='JSON do user cadastrado',
    status_code=status.HTTP_200_OK)
def busca_userID(id: int, response: Response):
    lista_user = findUser(id)
    if lista_user:
        response.status_code = status.HTTP_200_OK
        return JSONResponse(jsonable_encoder(lista_user))
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND


# Cadastro de users
@router.post(
    '/',
    summary='Cadastrar um novo user',
    description='Cadastra um novo user no banco de dados e retorna o user cadastrado',
    response_description='Retorna o user cadastrado',
    status_code=status.HTTP_200_OK)
def cadastraUser(user: User, response: Response):
    novoUser = createUser(user)
    if novoUser:
        response.status_code = status.HTTP_200_OK
        return JSONResponse(jsonable_encoder(novoUser))
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND


# Editar user

@router.patch(
    '/{id}',
    summary='Editar user com base no ID',
    status_code=status.HTTP_200_OK)

def editaUser(userID: int, user: User, response: Response):
    alunoEditado = editUser(userID, user)
    if alunoEditado:
        response.status_code = status.HTTP_200_OK
        return JSONResponse(content=jsonable_encoder(alunoEditado))
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND


# Deletar alunos

@router.delete(
    '/{id}',
    summary='Apaga user com base no ID especificado',
    status_code=status.HTTP_200_OK)
def apagaUser(id: int, response: Response):

    userApagado = deleteUser(id)
    if userApagado:
        response.status_code = status.HTTP_200_OK
        return {
            "mensagem": f"User com ID: {id} foi apagado com sucesso"
        }
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND
