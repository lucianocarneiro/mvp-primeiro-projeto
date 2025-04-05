# Projeto: Minhas Medidas (Backend)

Este projeto fornece uma API RESTful desenvolvida com **Flask** e **SQLAlchemy**, que permite cadastrar, exibir, buscar e excluir medições corporais de usuários. Ideal para aplicações de controle de medidas corporais como academias, nutricionistas ou uso pessoal.

## Versão
1.0.0

## Tecnologias Utilizadas

- Python 3.10+
- Flask
- Flask-OpenAPI3
- Flask-CORS
- SQLAlchemy
- Pydantic

---

## Estrutura do Projeto

```
.
├── app.py                  # Arquivo principal com as rotas da API
├── model/
│   ├── base.py             # Base declarativa do SQLAlchemy
│   └── medidas.py          # Modelo da tabela de medidas
├── schemas/
│   ├── medidas.py          # Schemas (Pydantic) de entrada e saída
│   └── error.py            # Schema de mensagens de erro
├── logger.py               # Configuração de logs (se existir)
└── requirements.txt        # Lista de dependências do projeto
```

---

## Como Executar Localmente

### 1. Clone o repositório:
```bash
git clone https://github.com/dipucriodigital/desenvolvimento-full-stack.git
cd seu-repo
```

### 2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências:
```bash
pip install -r requirements.txt
```

> Se você ainda não tem o `requirements.txt`, você pode gerar um com:
> ```bash
> pip freeze > requirements.txt
> ```

### 4. Execute a aplicação:
```bash
python app.py
```

Para executar a API  basta executar:

```
flask run --host 0.0.0.0 --port 5000
```

A API estará disponível em: [http://localhost:5000](http://localhost:5000)

---

Para reiniciar a aplicação, basta executar o comando a seguir:

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

## Endpoints Disponíveis

### `GET /`
Redireciona para a interface de documentação Swagger/OpenAPI.

### `POST /medida`
Cadastra uma nova medida.

**Body JSON:**
```json
{
  "nome_completo": "Luciano de Oliveira Carneiro",
  "data_criacao": "2025-03-25",
  "data_peso": "2025-03-25",
  "peso": 76.6,
  "busto": 103.01,
  "braco_direito": 28.9,
  "braco_esquerdo": 28.9,
  "cintura": 75.5,
  "umbigo": 87.5,
  "quadril": 108.5,
  "coxa_direita": 60.1,
  "coxa_esquerda": 60.2,
  "panturrilha_direita": 34.5,
  "panturrilha_esquerda": 34.5
}
```

### `GET /medidas?nome_completo=&data_peso=`
Busca uma medida por nome completo e data do peso.

### `GET /medidas/list`
Lista todas as medidas cadastradas no sistema.

### `DELETE /medidas`
Exclui uma medida com base no nome completo e na data do peso.

**Body JSON:**
```json
{
  "nome_completo": "Luciano de Oliveira Carneiro",
  "data_peso": "2025-03-25 00:00:00.000000"
}
```

---

## Observações
- Todas as datas devem estar no formato: `YYYY-MM-DD HH:MM:SS.ssssss`
- CORS está habilitado para qualquer origem (`*`), facilitando a integração com o frontend durante o desenvolvimento.

---

## Pontos de melhorias (sprint 2)
- Tela de Login: Incluir uma tela de login com cadastro de cliente básico (e-mail e nome).
- Separar as telas de cadastro da tela de login, isso deixará o sistema com um visual da tela principal do sistema mais agradável ao passar a tela de login.
- Melhorar as respostas do back end focado em tratativa de retorno de erro.

## Autor
Feito por Luciano Oliveira - Primeiro projeto - Cadastro de Medidas/MVP

