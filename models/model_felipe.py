from typing import Optional, List, Type
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

class New_Mei(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    
    # Esses dados sao preenchidos Automaticamente
    grupo_natureza_juridica: str = Field(default="Entidades empresariais")
    check_box_mei: bool = Field(default=True)
    natureza_juridica: int = Field(default="2135 - EMPRESARIO (INDIVIDUAL)")
    tipo_estabelecimento: str = Field(default="Matriz")
    
    # Esses dados sao fornecidos pelo requerente
    cpf: int = Field (nullable=False, unique=True)
    objetivo_viabilidade: str = Field (nullable= False)
    cnae: List["Ocupacao"] = Relationship(back_populates="cnae")
    cnae_secundario: List()

    inscricao_endereco: int = Field(nullable=False)    
    tipo_endereco: str = Field(nullable=False)    
    endereco: str = Field(nullable=False)    
    nr_endereco: str = Field(nullable=False)    

    
class Ocupacao(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    cnae: Optional[New_Mei] = Relationship(back_populates="cnae")
    descricao: str
