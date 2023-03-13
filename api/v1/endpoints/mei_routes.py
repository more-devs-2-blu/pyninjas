from fastapi import APIRouter, Response
from fastapi import status
from models.model import Nova_mei, Ocupacao, RelacaoOcupacaoXNovaMEI
from controller.novamei_controller import createMei, findMei, allCnaes

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

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
def criaMei(mei: Nova_mei, ocupacoes: List[int], response: Response):
    # relacoes_ocupacoes = []
    # for ocupacao in ocupacoes:
    #     relacao = RelacaoOcupacaoXNovaMEI(ocupacao=ocupacao)
    #     relacoes_ocupacoes.append(relacao)
    novo_mei = createMei(
        cpf=mei.cpf,
        objetivo_viabilidade=mei.objetivo_viabilidade,
        inscricao_endereco=mei.inscricao_endereco,
        tipo_endereco=mei.tipo_endereco,
        endereco=mei.endereco,
        nr_endereco=mei.nr_endereco,
        ocupacoes=ocupacoes
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
def buscaMei(response:Response, Nova_meiID: int=None, CPF: str=None):
    if not Nova_meiID and not CPF:
        response.status_code=status.HTTP_400_BAD_REQUEST
        return {'detail': 'É necessário fornecer ao menos um parâmetro de busca (ID ou cpf)'}
    
    finded_mei = findMei(Nova_meiID=Nova_meiID, CPF=CPF)
    if finded_mei:
        response.status_code=status.HTTP_200_OK
        return JSONResponse(content=jsonable_encoder(finded_mei))
    else:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'detail': 'Solicitação não encontrada'}
  

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
def listaCNAES(response: Response):
    all_cnaes = allCnaes()
    if all_cnaes:
        response.status_code = status.HTTP_200_OK
        return JSONResponse(content=jsonable_encoder(all_cnaes))
    else:
        response.status = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND

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