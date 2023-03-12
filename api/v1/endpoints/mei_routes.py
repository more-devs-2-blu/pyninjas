from controller.user_controller import editUser, createUser, deleteUser, findUser, allUsers
from fastapi import APIRouter, Response
from fastapi import status
from models.model import Nova_mei, Ocupacao, RelacaoOcupacaoXNovaMEI
from controller.novamei_felipe_teste import createMei

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlmodel import Session, select
from db.database import engine 
from typing import List

router = APIRouter()

# Envia a Solicitacao no Site
@router.post(
    '/novamei',
    summary='Envia uma nova Solicitação de MEI',
    description='Formulario para Abertura de MEI',
    status_code=status.HTTP_200_OK,
    tags=['MEI']
)
def criaMei(mei: Nova_mei, ocupacoes: List[Ocupacao], response: Response):
    relacoes_ocupacoes = []
    for ocupacao in ocupacoes:
        relacao = RelacaoOcupacaoXNovaMEI(ocupacao=ocupacao)
        relacoes_ocupacoes.append(relacao)
    novo_mei = createMei(
        cpf=mei.cpf,
        objetivo_viabilidade=mei.objetivo_viabilidade,
        inscricao_endereco=mei.inscricao_endereco,
        tipo_endereco=mei.tipo_endereco,
        endereco=mei.endereco,
        nr_endereco=mei.nr_endereco,
        relacao_ocupacoes=relacoes_ocupacoes
    )
    if novo_mei:
        response.status_code = status.HTTP_200_OK
        return JSONResponse(jsonable_encoder(novo_mei))
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND



# Busca a Solicitacao no Site
@router.get(
    '/buscamei',
    summary='Busca uma Solicitação no Site',
    description='Busca uma Solicitação por Codigo ou CPF',
    status_code=status.HTTP_200_OK,
    tags=['MEI']
)
def buscaMei():
    pass

# Edita a Solicitacao no Site
@router.post(
    '/novamei/{id}',
    summary='Edita uma Solicitação pelo Codigo ou CPF',
    description='Edita a Solicitação pelo ID',
    status_code=status.HTTP_200_OK,
    tags=['MEI']
)
def editarMei():
    pass

# Busca lista de CNAEs para MEI
@router.get(
    '/cnaes',
    summary='Exibe a Lista de CNAEs para MEI',
    description='Lista de CNAEs para MEI',
    status_code=status.HTTP_200_OK,
    tags=['CNAES']
)
def listaCNAEs():
    pass

# Busca lista de CNAEs registrada na Solicitacao da MEI
@router.get(
    '/cnaes/{id}',
    summary='Busca a Lista de CNAEs atrelada a uma determinada Solicitação',
    description='CNAEs atrelados a uma Solicitação Especifica',
    status_code=status.HTTP_200_OK,
    tags=['CNAES']
)
def buscaCNAEsporID():
    pass


