from db.database import engine
from datetime import datetime
from models.model import Nova_mei, Ocupacao, RelacaoOcupacaoXNovaMEI
from sqlmodel import Session

def createMei(cpf: str, objetivo_viabilidade: str, inscricao_endereco: str, tipo_endereco: str, endereco: str, nr_endereco: str, ocupacoes: list[str]):
    with Session(engine) as session:
        nova_mei = Nova_mei(
            grupo_natureza_juridica="Entidades empresariais",
            check_box_mei=True,
            natureza_juridica="2135 - EMPRESARIO (INDIVIDUAL)",
            tipo_estabelecimento="Matriz",
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
        
        ocupacoes_list = []
        for ocupacao_descricao in ocupacoes:
            ocupacao = session.query(Ocupacao).filter_by(descricao=ocupacao_descricao).first()
            if not ocupacao:
                ocupacao = Ocupacao(descricao=ocupacao_descricao)
                session.add(ocupacao)
                session.commit()
                session.refresh(ocupacao)
            
            ocupacoes_list.append(ocupacao)
            
            nova_mei_ocupacao = RelacaoOcupacaoXNovaMEI(nova_mei_id=nova_mei.id, ocupacao_id=ocupacao.id, is_primario=True)
            session.add(nova_mei_ocupacao)
            session.commit()

        nova_mei.relacao_ocupacoes = ocupacoes_list
        
        session.commit()
        session.refresh(nova_mei)
        
        return nova_mei

with Session(engine) as session:
    nova_mei = Nova_mei(cpf="12345678900",  objetivo_viabilidade="teste",
                        inscricao_endereco="123", tipo_endereco="Rua", endereco="Rua Teste",
                        nr_endereco="123")
    ocupacao = Ocupacao(descricao="Teste", cnae="123")
    relacao_ocupacao = RelacaoOcupacaoXNovaMEI(nova_mei=nova_mei, ocupacao=ocupacao, is_primario=True)


    session.add(nova_mei)
    session.add(ocupacao)
    session.commit()

    print(nova_mei)
    print(ocupacao)