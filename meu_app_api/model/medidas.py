from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from datetime import datetime, date
from typing import Union
from  model import Base

class Medidas(Base):

#declarando o nome da tabela
    __tablename__ = 'medidas'
    
#criando as colunas da tabela de medidas
    id = Column("pk_medida", Integer, primary_key=True)
    data_criacao = Column(DateTime, default=datetime.now) #criação automática para o dia de hoje, não será exibido no fron-end
    data_peso = Column(DateTime) # Essa data será exibida no front end e será inclusa manualmente pelo usuário.
    nome_completo = Column(String(4000)) #Nome completo, ex: Luciano de Oliveira Carneiro
    peso = Column(Float) #ex: 76,6
    busto = Column(Float) #ex: 103,01
    braco_direito = Column(Float) #ex: 28,5
    braco_esquerdo = Column(Float) #ex: 28,5
    cintura = Column(Float) #ex: 76,5
    umbigo = Column(Float) #ex: 87,5
    quadril = Column(Float) #ex: 108,5
    coxa_direita = Column(Float) #ex: 60,1
    coxa_esquerda = Column(Float) #ex: 60,1
    panturrilha_direita = Column(Float) #ex: 34,5
    panturrilha_esquerda = Column(Float) #ex: 34,5
    
#essa tabela não terá relacionamento com outra tabela por ser um MVP.

#método de constructor da classe de criação das medidas na base de dados
def __init__(self, data_peso=DateTime, nome_completo=str, peso=float, busto=float, braco_direito=float, braco_esquerdo=float, cintura=float, umbigo=float, quadril=float, coxa_direita=float, coxa_esquerda=float, panturrilha_direita=float, panturrilha_esquerda=float):
    """
        Tabela de medidas criada na tela de criação de medidas do front end.

        Arguments:
            data_criacao: criação automática para o dia de hoje, não será exibido no fron-end
            data_peso: Essa data será exibida no front end e será inclusa manualmente pelo usuário
            nome_completo: nome completo do usuário, ex: Luciano de Oliveira Carneiro
            peso:  ex: 76,6
            busto: ex: 103,01
            braco_direito: ex: 28,5
            braco_esquerdo: ex: 28,5
            cintura: ex: 76,5
            umbigo: ex: 87,5
            quadril: ex: 108,5
            coxa_direita: ex: 60,1
            coxa_esquerda: ex: 60,1
            panturrilha_direita: ex: 34,5
            panturrilha_esquerda: ex: 34,5               
        """
    
    #apropriando os valores na chamada    
    self.data_criacao = datetime.now()
    self.data_peso = data_peso
    self.nome_completo = nome_completo
    self.peso = peso
    self.busto = busto
    self.braco_direito = braco_direito
    self.braco_esquerdo = braco_esquerdo
    self.cintura = cintura
    self.umbigo = umbigo
    self.quadril = quadril
    self.coxa_direita = coxa_direita
    self.coxa_esquerda = coxa_esquerda
    self.panturrilha_direita = panturrilha_direita
    self.panturrilha_esquerda = panturrilha_esquerda