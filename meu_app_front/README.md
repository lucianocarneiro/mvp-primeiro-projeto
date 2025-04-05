# 📏 Cadastro e Consulta de Medidas - Front-end

Este é o front-end de um sistema simples para **cadastro, consulta e exclusão de medidas corporais**. Ele se comunica com um back-end via API REST utilizando `fetch` com métodos `GET`, `POST` e `DELETE`.

## 🔧 Tecnologias Utilizadas

- HTML5
- CSS3
- JavaScript puro (vanilla JS)
- API REST (conexão com back-end Flask)
- Google Fonts (Poppins)
- Ícones (Flaticon)

## 📂 Estrutura de Arquivos

## ✅ Funcionalidades

### Cadastro de Medidas
- Formulário para inserir nome, data da pesagem e várias medidas corporais.
- Validação básica para garantir preenchimento de todos os campos.
- Envio de dados via `POST` para o servidor.

### Consulta de Medidas
- Filtro por nome e data.
- Retorno dos registros consultados em uma tabela organizada.
- Possibilidade de deletar registros diretamente na tabela.

### Exclusão
- Exclusão de um registro por nome e data de pesagem.
- Confirmação de exclusão com `confirm()`.

## 🔌 Comunicação com o Back-end

- `GET` ➝ `/medidas/list`  
  Recupera todos os registros cadastrados.

- `POST` ➝ `/medida`  
  Cadastra um novo registro.

- `DELETE` ➝ `/medidas?nome_completo=...&data_peso=...`  
  Deleta um registro específico.

> ⚠️ O front está configurado para comunicar-se com o servidor local (`http://127.0.0.1:5000`).  
> Verifique se o back-end Flask está rodando nessa porta.

## 🎨 Estilo

O projeto utiliza um fundo com imagem personalizada, layout responsivo em grid para os formulários, bordas arredondadas e `backdrop-filter` para efeito de desfoque nos containers.

## 📸 Preview

<img src="photos/measuring_tape.jpg" width="400" alt="Imagem de fundo utilizada">

## 🚀 Como Rodar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git

---


## Autor
Feito por Luciano Oliveira - Primeiro projeto - Cadastro de Medidas/MVP