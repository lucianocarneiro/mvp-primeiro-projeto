from pydantic import BaseModel
from typing import Optional, List
from model.medidas import Medidas
from datetime import datetime, date #import de modelo de data para utilizar na documentação e modelo de dados(ex: MedidasBuscaSchema)

class MedidasBuscaSchema(BaseModel):
    """ Define como uma medida será retornada.
    """
    nome: str = "Luciano de Oliveira Carneiro"
    data_peso: str = "2025-03-25 00:00:00.000000"
    
class MedidasBuscaListaSchema(BaseModel):
    """ Define como uma lista de medidas será retornada.
    """
    nome: str = "Luciano de Oliveira Carneiro"

class MedidasViewSchema(BaseModel):
    """ Define como a medida será retornada.
    """
    id: int = "1"
    nome: str = "Luciano de Oliveira Carneiro"
    data_peso: datetime
    
class MedidasDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção de dados.
    """
    id: int = 1
    nome: str = "Luciano de Oliveira Carneiro"
    data_peso: datetime
    peso_del: str = "X"
    
class MedidasSchema(BaseModel):
    """ Define como uma nova medida a ser inserido deve ser representado
    """
    data_criacao: datetime = "2025-03-25"
    data_peso: date = "2025-03-25"
    nome_completo: str = "Luciano de Oliveira Carneiro"
    peso: float = "76.6"
    busto: float = "103.01"
    braco_direito: float = "28.9"
    braco_esquerdo: float = "28.9"
    cintura: float = "75.5"
    umbigo: float = "87.5"
    quadril: float = "108.5"
    coxa_direita: float = "60.1"
    coxa_esquerda: float = "60.2"
    panturrilha_direita: float = "34.5"
    panturrilha_esquerda: float = "34.5"

class ListagemMedidasSchema(BaseModel):
    """ Define como uma listagem de medidas será retornada.
    """
    medidas:List[MedidasSchema]


def apresenta_medidas(medidas: Medidas):
    """ Retorna uma representação da medida seguindo o schema definido em
        MedidasViewSchema.
    """
    return {
        "id": medidas.id,
        "nome": medidas.nome_completo,
        "data_peso": medidas.data_peso,
        "data_criacao": medidas.data_criacao,
        "peso": medidas.peso,
        "busto": medidas.busto,
        "braco_direito": medidas.braco_direito,
        "braco_esquerdo": medidas.braco_esquerdo,
        "cintura": medidas.cintura,
        "umbigo": medidas.umbigo,
        "quadril": medidas.quadril,
        "coxa_direita": medidas.coxa_direita,
        "coxa_esquerda": medidas.coxa_esquerda,
        "panturrilha_direita": medidas.panturrilha_direita,
        "panturrilha_esquerda": medidas.panturrilha_esquerda
    }
    
