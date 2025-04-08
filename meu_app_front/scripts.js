/*
  --------------------------------------------------------------------------------------
  Função para obter as medidas existentes no servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getMedidasList = async () => {
  const nomeFiltro = document.getElementById('nomeConsulta').value.toLowerCase();
  const dataFiltro = document.getElementById('dataConsulta').value;

  let url = 'http://127.0.0.1:5000/medidas/list';

  fetch(url, {
    method: 'GET',
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Retorno do Back end:", data);

      clearTable();

      data.medidas
        .filter(item => {
          const nomeValido = !nomeFiltro || item.nome.toLowerCase().includes(nomeFiltro);
          const dataFormatada = formatDate(item.data_peso); // transforma data do backend em yyyy-mm-dd
          const dataValida = !dataFiltro || dataFormatada === dataFiltro;
          return nomeValido && dataValida;
        })
        .forEach(item => insertList(
          item.nome,
          formatDate(item.data_peso),
          formatDate(item.data_criacao),
          item.peso,
          item.busto,
          item.braco_direito,
          item.braco_esquerdo,
          item.cintura,
          item.umbigo,
          item.quadril,
          item.coxa_direita,
          item.coxa_esquerda,
          item.panturrilha_direita,
          item.panturrilha_esquerda
        ));
    })
    .catch((error) => {
      console.error('Erro ao buscar dados:', error);
    });
    
   
};
/*
  --------------------------------------------------------------------------------------
  Chamada da função para exibição dos valores existentes na base
  --------------------------------------------------------------------------------------
*/
// Chama a função ao carregar a página
// document.addEventListener('DOMContentLoaded', getMedidasList);

/*
  --------------------------------------------------------------------------------------
  Função para incluir um item de medida na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postMedidas = async (
  nome_completo, data_peso, data_criacao, peso, busto,
  braco_direito, braco_esquerdo, cintura, umbigo,
  quadril, coxa_direita, coxa_esquerda,
  panturrilha_direita, panturrilha_esquerda
) => {
  try {
    const formData = new FormData();
    formData.append('nome_completo', nome_completo);
    formData.append('data_peso', data_peso);
    formData.append('data_criacao', data_criacao);
    formData.append('peso', peso);
    formData.append('busto', busto);
    formData.append('braco_direito', braco_direito);
    formData.append('braco_esquerdo', braco_esquerdo);
    formData.append('cintura', cintura);
    formData.append('umbigo', umbigo);
    formData.append('quadril', quadril);
    formData.append('coxa_direita', coxa_direita);
    formData.append('coxa_esquerda', coxa_esquerda);
    formData.append('panturrilha_direita', panturrilha_direita);
    formData.append('panturrilha_esquerda', panturrilha_esquerda);

    let url = 'http://127.0.0.1:5000/medida';
    const response = await fetch(url, {
      method: 'POST',
      body: formData
    });

    if (!response.ok) {
      throw new Error('Erro ao enviar medidas');
    }

    const data = await response.json();
      console.log('Sucesso:', data);
      alert('Registro criado com sucesso!');

    // limpando os campos
    document.getElementById("nomeCompleto").value = "";
    document.getElementById("dataPesagem").value = "";
    document.getElementById("peso").value = "";
    document.getElementById("busto").value = "";
    document.getElementById("bracoDireito").value = "";
    document.getElementById("bracoEsquerdo").value = "";
    document.getElementById("cintura").value = "";
    document.getElementById("umbigo").value = "";
    document.getElementById("quadril").value = "";
    document.getElementById("coxaDireita").value = "";
    document.getElementById("coxaEsquerda").value = "";
    document.getElementById("panturrilhaDireita").value = "";
    document.getElementById("panturrilhaEsquerda").value = "";

  } catch (error) {
      console.error('Erro:', error);
  }

};

/*
  --------------------------------------------------------------------------------------
  Função para inserir itens na lista apresentada no container de consulta do HTML
  --------------------------------------------------------------------------------------
*/
const insertList = (nome_completo, data_peso, data_criacao, peso, busto,
  braco_direito, braco_esquerdo, cintura, umbigo,
  quadril, coxa_direita, coxa_esquerda,
  panturrilha_direita, panturrilha_esquerda) => {

  const item = [nome_completo, data_peso, data_criacao, peso, busto,
    braco_direito, braco_esquerdo, cintura, umbigo,
    quadril, coxa_direita, coxa_esquerda,
    panturrilha_direita, panturrilha_esquerda];

  const table = document.getElementById('myTable');
  const row = table.insertRow();

  // Cria a célula do ícone de delete
  const deleteCell = row.insertCell(0);
  const img = document.createElement('img');
  img.src = 'https://cdn-icons-png.flaticon.com/512/126/126468.png';
  img.alt = 'Excluir';
  img.width = 13;
  img.height = 13;
  img.style.cursor = 'pointer';
  img.title = 'Excluir registro';
  
  img.onclick = () => {
    deleteMedida(nome_completo, data_peso); // aqui você pode ajustar os parâmetros conforme necessário
  };

  deleteCell.appendChild(img);

  // Preenche o resto da linha com os dados
  for (let i = 0; i < item.length; i++) {
    const cel = row.insertCell(i + 1); // Começa do índice 1 pois a célula 0 já é o ícone
    cel.textContent = item[i];
  }
};

/*
  --------------------------------------------------------------------------------------
  Chamada da função chamada para consultar as medidas
  --------------------------------------------------------------------------------------
*/
const buttonConsultarMedida = () => {
  getMedidasList();
  
};


/*
  --------------------------------------------------------------------------------------
  Função para limpar tabela myTable
  --------------------------------------------------------------------------------------
*/
const clearTable = () => {
  const table = document.getElementById('myTable');

  // Remove todas as linhas exceto a primeira (cabeçalho)
  while (table.rows.length > 1) {
    table.deleteRow(1);
  }
};


/*
  --------------------------------------------------------------------------------------
  Função para tratar a data recebida da base de dados
  --------------------------------------------------------------------------------------
*/
const formatDate = (dataString) => {
  const date = new Date(dataString);
  return date.toISOString().split('T')[0]; // retorna "yyyy-mm-dd"
};

/*
  --------------------------------------------------------------------------------------
  Método deletar medida exibida nna lista
  --------------------------------------------------------------------------------------
*/

const deleteMedida = async (nome_completo, data_peso) => {
  const confirmDelete = confirm(`Deseja realmente excluir o registro de ${nome_completo} em ${data_peso}?`);
  if (!confirmDelete) return;

  const dataFormatada = `${data_peso} 00:00:00.000000`;

  const url = `http://127.0.0.1:5000/medidas?nome_completo=${encodeURIComponent(nome_completo)}&data_peso=${encodeURIComponent(dataFormatada)}`;

  try {
    const response = await fetch(url, {
      method: 'DELETE',
    });

    if (!response.ok) {
      throw new Error('Erro ao deletar a medida');
    }

    alert('Registro deletado com sucesso!');
    getMedidasList(); // atualiza a tabela após exclusão
  } catch (error) {
    console.error('Erro ao deletar medida:', error);
    alert('Falha ao excluir o registro.');
  }
};
/*
  --------------------------------------------------------------------------------------
  Transformar data para consulta no beck end
  --------------------------------------------------------------------------------------
*/

const formatDateForBackend = (dateString) => {
  // Transforma "2025-03-25" em "2025-03-25 00:00:00.000000"
  return `${dateString} 00:00:00.000000`;
};



/*
  --------------------------------------------------------------------------------------
  Chamada do método post para criar um registro no servidor
  --------------------------------------------------------------------------------------
*/

const buttonNovaMedida = () => {
    const nome_completo = document.getElementById("nomeCompleto").value;
    const data_peso = document.getElementById("dataPesagem").value;
    const data_criacao = new Date().toISOString().split('T')[0]; // data de hoje no formato yyyy-mm-dd
    const peso = document.getElementById("peso").value;
    const busto = document.getElementById("busto").value;
    const braco_direito = document.getElementById("bracoDireito").value;
    const braco_esquerdo = document.getElementById("bracoEsquerdo").value;
    const cintura = document.getElementById("cintura").value;
    const umbigo = document.getElementById("umbigo").value;
    const quadril = document.getElementById("quadril").value;
    const coxa_direita = document.getElementById("coxaDireita").value;
    const coxa_esquerda = document.getElementById("coxaEsquerda").value;
    const panturrilha_direita = document.getElementById("panturrilhaDireita").value;
    const panturrilha_esquerda = document.getElementById("panturrilhaEsquerda").value;
  
    // Checagem básica se está tudo preenchido
    if (
      !nome_completo || !data_peso || !peso || !busto || !braco_direito || !braco_esquerdo ||
      !cintura || !umbigo || !quadril || !coxa_direita || !coxa_esquerda ||
      !panturrilha_direita || !panturrilha_esquerda
    ) {
      document.querySelector('.error_login').style.display = 'block';
      return;
    } else {
      document.querySelector('.error_login').style.display = 'none';
    }
  
    postMedidas(
      nome_completo,
      data_peso,
      data_criacao,
      peso,
      busto,
      braco_direito,
      braco_esquerdo,
      cintura,
      umbigo,
      quadril,
      coxa_direita,
      coxa_esquerda,
      panturrilha_direita,
      panturrilha_esquerda
    );
  };