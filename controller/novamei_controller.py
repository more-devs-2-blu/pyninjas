from db.database import engine
from datetime import datetime
from models.model import Nova_mei, RelacaoOcupacaoXNovaMEI, Ocupacao
from sqlmodel import Session, select
from typing import List
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


# Função Criar Mei
def createMei(cpf: str, objetivo_viabilidade: str, inscricao_endereco: str, tipo_endereco: str, endereco: str, nr_endereco: str, ocupacoes: List[int] = None):   # Criação da Instancia no Banco de Dados
    with Session(engine) as session:
        nova_mei = Nova_mei(
            cpf=cpf,
            objetivo_viabilidade=objetivo_viabilidade,
            inscricao_endereco=inscricao_endereco,
            tipo_endereco=tipo_endereco,
            endereco=endereco,
            nr_endereco=nr_endereco,
        )

        session.add(nova_mei)
        session.commit()
        session.refresh(nova_mei)

        for i in range(len(ocupacoes)): 
            is_primario = True if i == 0 else False
            cnae = RelacaoOcupacaoXNovaMEI(
                nova_mei_id=nova_mei.id,
                ocupacao_id=ocupacoes[i],
                is_primario=is_primario)
            session.add(cnae)
            session.commit()

        return nova_mei


def findMei(Nova_meiID: int = None, CPF: str = None):
    with Session(engine) as session:
        query = select(Nova_mei, RelacaoOcupacaoXNovaMEI).join(RelacaoOcupacaoXNovaMEI)
        
        if Nova_meiID:
            query = query.where(Nova_mei.id == Nova_meiID)
        elif CPF:
            query = query.where(Nova_mei.cpf == CPF)
        
        results = session.exec(query).all()
        return results

def updateMei(mei_id: int, mei: Nova_mei, ocupacoes: List[int] = None):
    # Busca o MEI no banco de dados
    with Session(engine) as session:
        edit_mei = session.get(Nova_mei, mei_id)
        if edit_mei is None:
            raise HTTPException(status_code=404, detail="MEI não encontrado")
        
        # Atualiza os dados do MEI
        edit_mei.cpf = mei.cpf
        edit_mei.objetivo_viabilidade = mei.objetivo_viabilidade
        edit_mei.inscricao_endereco = mei.inscricao_endereco
        edit_mei.tipo_endereco = mei.tipo_endereco
        edit_mei.endereco = mei.endereco
        edit_mei.nr_endereco = mei.nr_endereco



        # Remove todas as relações antigas de ocupação
        for relacao in edit_mei.relacao_ocupacoes:
            session.delete(relacao)

        # Cria novas relações para as ocupações fornecidas
        for i in range(len(ocupacoes)): 
            is_primario = True if i == 0 else False
            cnae = RelacaoOcupacaoXNovaMEI(
                nova_mei_id=edit_mei.id,
                ocupacao_id=ocupacoes[i],
                is_primario=is_primario)
            
            session.add(cnae)
           
        session.commit()
        session.refresh(edit_mei)

        return JSONResponse(jsonable_encoder(edit_mei))



def pesquisaCnaes(descricao: str = None, cnae: str = None):
    with Session(engine) as session:
        statement = select(Ocupacao)
        if descricao is not None:
            statement = statement.filter(Ocupacao.descricao.like(f'%{descricao.upper()}%'))
        if cnae is not None:
            statement = statement.filter(Ocupacao.cnae.like(f'%{cnae}%'))
        
        results = session.exec(statement).all()
        return results
    
    
    
def listaCnaes():
    with Session(engine) as session:
        statement = select(Ocupacao)
        
        results = session.exec(statement).all()
        return results