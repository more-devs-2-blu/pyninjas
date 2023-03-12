from typing import Optional, List, Type
from sqlmodel import Field, SQLModel, Relationship

# class New_Mei(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    
#     # Esses dados sao preenchidos Automaticamente
#     grupo_natureza_juridica: str = Field(default="Entidade Empresarial")
#     check_box_mei: bool = Field(default=True)
#     natureza_juridica: int = Field(default=2135)
#     tipo_estabelecimento: str = Field(default="Matriz")
    
#     # Esses dados sao fornecidos pelo requerente
#     cpf: int = Field()
#     objetivo_viabilidade: str
#     cnae: List["Ocupacao"]
#     cnae_secundario: List()

#     inscricao_endereco: int    
#     tipo_endereco: str
#     endereco: str
#     nr_endereco: str

    
class Ocupacao(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    descricao: str = Field()
    cnae: str = Field()



