from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship



class Nova_mei(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    
    # Esses dados sao preenchidos Automaticamente
    grupo_natureza_juridica: str = Field(default="Entidades empresariais")
    check_box_mei: bool = Field(default=True)
    natureza_juridica: str = Field(default="2135 - EMPRESARIO (INDIVIDUAL)")
    tipo_estabelecimento: str = Field(default="Matriz")
    
    # Esses dados sao fornecidos pelo requerente
    cpf: str = Field (nullable=False) #unique=True
    objetivo_viabilidade: str = Field (nullable= False)


    inscricao_endereco: str = Field(nullable=False)    
    tipo_endereco: str = Field(nullable=False)    
    endereco: str = Field(nullable=False)    
    nr_endereco: str = Field(nullable=False)

    relacao_ocupacoes: List["RelacaoOcupacaoXNovaMEI"] = Relationship(back_populates="nova_mei")

    
    
class Ocupacao(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    descricao: str = Field()
    cnae: str = Field()    


class RelacaoOcupacaoXNovaMEI(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    nova_mei_id: int = Field(default=None, foreign_key="nova_mei.id")
    ocupacao_id: int = Field(default=None, foreign_key="ocupacao.id")
    is_primario: bool = Field(default=True)
    
    nova_mei: Optional[Nova_mei] = Relationship(back_populates="relacao_ocupacoes")