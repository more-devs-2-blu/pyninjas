from db.database import engine
from datetime import datetime
from models.model import Nova_mei, RelacaoOcupacaoXNovaMEI, Ocupacao
from sqlmodel import Session, select
from typing import List


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

def findMei(Nova_meiID: int):
    with Session(engine) as session:
        statement = select(Nova_mei, RelacaoOcupacaoXNovaMEI).join(RelacaoOcupacaoXNovaMEI).where(Nova_mei.id == Nova_meiID)
        results = session.exec(statement).first()
        return results

    

def allCnaes():
    with Session(engine) as session:
        statement = select(Ocupacao)
        
        results = session.exec(statement).all()
        return results