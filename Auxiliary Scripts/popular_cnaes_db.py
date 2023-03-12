import pandas as pd
from sqlmodel import Session
from database import engine
from models.model import Ocupacao

data = pd.read_csv('lista_de_cnaes(mei).csv', sep=';', header=None)

ocupacoes = []

# Loop que percorre a lista (Arquivo CSV) e cria os objetos de Ocupacao
for index, row in data.iterrows():
    desc = row.iloc[0]
    cnae = row.iloc[1]
    nova_ocupacao = Ocupacao(
        id=None,
        descricao=desc,
        cnae=cnae
    )
    # Adiciona os objetos na lista ocupacoes.
    ocupacoes.append(nova_ocupacao)
            
# Aqui adicionamos todos os objetos ao banco de dados
with Session(engine) as session:
    session.add_all(ocupacoes)
    session.commit()

