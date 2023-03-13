from fastapi import APIRouter, Response
from fastapi import status
from models.model import Nova_mei, Ocupacao, RelacaoOcupacaoXNovaMEI
from controller.novamei_controller import createMei, findMei, pesquisaCnaes, updateMei
from sqlmodel import Session, select

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
        return {'detail': 'É necessário fornecer ao menos um parâmetro de busca (ID ou CPF)'}
    
    finded_mei = None
    if Nova_meiID is not None:
        finded_mei = findMei(Nova_meiID=Nova_meiID)
    elif CPF is not None:
        finded_mei = findMei(CPF=CPF)

    if finded_mei:
        response.status_code = status.HTTP_200_OK
        return JSONResponse(content=jsonable_encoder(finded_mei))
    else:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'detail': 'Solicitação não encontrada'}
  

# Edita a Solicitacao no Site
@router.patch(
    '/editamei',
    summary='Edita uma Solicitação pelo Codigo ou CPF',
    description='Edita a Solicitação pelo ID',
    status_code=status.HTTP_200_OK,
    tags=['MEI']
)
def editarMei(mei_id: int, mei: Nova_mei, ocupacoes: List[int], response: Response):
    meiEditado = updateMei(mei_id, mei, ocupacoes)
    if not meiEditado:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {'detail': f'MEI com ID {mei_id} não encontrado.'}

    # retorna o MEI atualizado
    response.status_code = status.HTTP_200_OK
    return JSONResponse(jsonable_encoder(meiEditado))
    


# Pesquisa a lista de Ocupacao por descricao ou codigo de CNAEs
@router.get(
    '/cnaes',
    summary='Pesquisa a Ocupação MEI por descrição ou código CNAE',
    description='Pesquisa a Ocupação MEI por descrição ou código MEI',
    status_code=status.HTTP_200_OK,
    tags=['CNAES']
)
def pesquisaCNAES(response: Response, descricao: str = None, cnae: str = None):
    if descricao is None and cnae is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"detail": "Por favor, forneça pelo menos uma descrição ou um código CNAE."}
    pesquisa_cnaes = pesquisaCnaes(descricao,cnae)
    if pesquisa_cnaes:
        response.status_code = status.HTTP_200_OK
        return JSONResponse(content=jsonable_encoder(pesquisa_cnaes))
    else:
        response.status = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND

#Busca a lista de todos os CNAEs
@router.get(
    '/lista_cnaes',
    summary='Busca a lista de todos os CNAEs',
    description='Busca a lista de todos os CNAEs',
    status_code=status.HTTP_200_OK,
    tags=['CNAES']
)
def listaCNAES(response: Response):
    lista_cnaes = pesquisaCnaes()
    if lista_cnaes:
        response.status_code = status.HTTP_200_OK
        return JSONResponse(content=jsonable_encoder(lista_cnaes))
    else:
        response.status = status.HTTP_404_NOT_FOUND
        return status.HTTP_404_NOT_FOUND