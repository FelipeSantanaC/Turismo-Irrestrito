const registerButton = document.querySelector('#register-button');
const closeRegisterButton = document.querySelector('#closeButtonCadastro');
const modal = document.querySelector('#modalCadastro')

registerButton.addEventListener('click', () =>{
    modal.showModal();

})

closeRegisterButton.addEventListener('click', () =>{
    modal.close();
})

// Função que é chamada quando o botão de cadastro é clicado
function cadastrar() {
  // Obtém os valores dos campos de entrada
  var nomeCompleto = document.getElementById('nomeCompleto').value;
  var email = document.getElementById('email').value;
  var senha = document.getElementById('senha').value;

  // Cria um objeto com os dados do usuário
  var userData = {
    name: nomeCompleto,
    email: email,
    password: senha
  };

  // Envia uma solicitação POST para a API do Django
  fetch('/api/myapp/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(userData)
  })
  .then(response => response.json())
  .then(data => {
    // O cadastro foi bem-sucedido, redirecione para a página index
    window.location.href = '/';
  })
  .catch(error => {
    // Ocorreu um erro ao cadastrar o usuário
    console.error('Erro ao cadastrar usuário:', error);
  });
}

// Adicione um ouvinte de evento ao botão de cadastro
document.getElementById('buttonCadastrar').addEventListener('click', cadastrar);
