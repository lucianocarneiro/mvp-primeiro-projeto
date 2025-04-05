from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError #utilizadas para tratar erros de integradade de banco de dados

from model import Session, Medidas, base
from logger import logger
from schemas import error, medidas
from flask_cors import CORS
from datetime import datetime
from schemas.medidas import apresenta_medidas, MedidasDelSchema


# faz a configuração inicial da aplicação Flask com a integração do Flask-OpenAPI3 e CORS
# __name__ = script atual
info = Info(title="Minhas Medidas", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET", "POST", "DELETE", "PUT", "OPTIONS"])

# definindo tags já passando o nome e a descrição
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
medidas_tag = Tag(name="Medidas", description="Funcionalidades da API: get, put, delete, post")

"------------ GET ------------"
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.get('/medidas', tags=[medidas_tag], 
         responses={"200": medidas.MedidasViewSchema, "404": error.ErrorSchema})
def get_medidas(query: medidas.MedidasBuscaSchema):
    """Faz a busca de um produto a partir do nome completo do usuário.
    """
    medidas_nome = query.nome
    #medidas_data = query.data_peso
    
    try:
        medidas_data = datetime.strptime(query.data_peso, "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        return {"message": "Formato inválido para data_peso. Use: YYYY-MM-DD HH:MM:SS.ssssss"}, 400
    
    print(medidas_data)
    print(medidas_nome)
    # criando conexão com a base
    session = Session()
    # fazendo a busca com as duas condições que é nome completo e data do peso
    medidas = session.query(Medidas).filter(Medidas.nome_completo == medidas_nome, Medidas.data_peso == medidas_data).first()

    if not medidas:
        # se a medida não foi encontrada
        error_msg = "Medida não encontrada na base :/"
        logger.debug(f"Coletando dados sobre a medida #{medidas_nome}")
        return {"message": error_msg}, 404
    else:
        # retorna a representação da medida
        return apresenta_medidas(medidas), 200
    
    
"------------ POST ------------"
"------------ POST ------------"
@app.post('/medida', tags=[medidas_tag],
          responses={"200": medidas.MedidasViewSchema, "409": error.ErrorSchema, "400": error.ErrorSchema})
def add_medidas(form: medidas.MedidasSchema):
    """Adiciona uma nova Medida à base de dados.

    Retorna uma representação das medidas existente no banco de dados.
    """
    medida = Medidas(
        nome_completo=form.nome_completo,
        data_peso=form.data_peso,
        data_criacao=form.data_criacao,
        peso=form.peso,
        busto=form.busto,
        braco_direito=form.braco_direito,
        braco_esquerdo=form.braco_esquerdo,
        cintura=form.cintura,
        umbigo=form.umbigo,
        quadril=form.quadril,
        coxa_direita=form.coxa_direita,
        coxa_esquerda=form.coxa_esquerda,
        panturrilha_direita=form.panturrilha_direita,
        panturrilha_esquerda=form.panturrilha_esquerda
    )
    
    try:
        # criando conexão com a base
        session = Session()
        # adicionando medidas
        session.add(medida)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado medida com o nome: '{medida.nome_completo}'")
        return medidas.apresenta_medidas(medida), 200

    except IntegrityError:
        session.rollback()
        return {"message": "Erro de integridade, a medida já existe!"}, 409
    
    
    
"------------ DELETE ------------"
@app.delete('/medidas', tags=[medidas_tag],
           responses={"200": medidas.MedidasDelSchema, "404": error.ErrorSchema})
def delete_medidas(query: medidas.MedidasBuscaSchema):
    """Deleta uma medida da base de dados a partir do nome completo e da data do peso."""

    medidas_nome = query.nome_completo
    
    try:
        medidas_data = datetime.strptime(query.data_peso, "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        return {"message": "Formato inválido para data_peso. Use: YYYY-MM-DD HH:MM:SS.ssssss"}, 400
    
    # Criando conexão com a base de dados
    session = Session()
    
    # Buscando a medida específica pelo nome completo e data_peso
    medida = session.query(Medidas).filter(Medidas.nome_completo == medidas_nome, Medidas.data_peso == medidas_data).first()

    if not medida:
        # Se a medida não for encontrada, retorna erro 404
        print(medidas_nome)
        error_msg = f"Medida não encontrada na base para a consulta nome:{medidas_nome} e data:{medidas_data}"
        logger.debug(f"Tentativa de deletar medida inexistente: {medidas_nome}")
        return {"message": error_msg}, 404

    # Se for encontrada a medida no banco, faremos o processo do método DELETE no banco
    session.delete(medida)
    session.commit()
    
    logger.debug(f"Medida removida: {medidas_nome} - {medidas_data}")
    return {"message": "Medida removida com sucesso!", "nome": medidas_nome,"peso_del": "X"}, 200

"------------ GET LIST ------------"
@app.get('/medidas/list', tags=[medidas_tag],
         responses={"200": medidas.ListagemMedidasSchema, "404": error.ErrorSchema})
def get_medidas_list(query: medidas.MedidasBuscaListaSchema):
    """Faz a busca por todas as Medidas cadastradas

    Retorna uma representação da listagem das medidas.
    """
    logger.debug(f"Coletando produtos ")
    # criando conexão com o banco de dados
    session = Session()
    
    # Realizando a consulta no banco com os filtros de nome e data_peso
    medidas_query = session.query(Medidas)
    medidas = medidas_query.all()
    
    if not medidas:
        # Caso não encontre nenhuma medida que atenda aos filtros
        return {"produtos": []}, 200
    else:
        # Retorna a lista com as medidas encontradas
        return {"medidas": [apresenta_medidas(medida) for medida in medidas]}, 200