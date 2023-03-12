from controller.user_controller import editUser, createUser, deleteUser, findUser, allUsers
from fastapi import APIRouter, Response
from fastapi import status
from models.model import Nova_mei, Ocupacao, RelacaoOcupacaoXNovaMEI

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter()

# Envia a Solicitacao no Site
@router.post(
    '/novamei',
    summary='Envia uma nova Solicitação de MEI',
    description='Formulario para Abertura de MEI',
    status_code=status.HTTP_200_OK,
    tags=['MEI']
)
def criaMei():
    pass

# Busca a Solicitacao no Site
@router.get(
    '/buscamei',
    summary='',
    tags=['MEI']
)
def buscaMei():
    pass

# Edita a Solicitacao no Site
@router.post(
    '/novamei/{id}',
    tags=['MEI']
)
def editarMei():
    pass

# Busca lista de CNAEs para MEI
@router.get(
    '/cnaes',
    tags=['CNAES']
)
def listaCNAEs():
    pass

# Busca lista de CNAEs registrada na Solicitacao da MEI
@router.get(
    '/cnaes/{id}',
    tags=['CNAES']
)
def buscaCNAEsporID():
    pass


