const registerButton = document.querySelector('#register-button');
const closeRegisterButton = document.querySelector('#closeButtonCadastro');
const modal = document.querySelector('#modalCadastro')

registerButton.addEventListener('click', () =>{
    modal.showModal();

})

closeRegisterButton.addEventListener('click', () =>{
    modal.close();
})

const loginButton = document.querySelector('#login-button');
const closeLoginButton = document.querySelector('#closeButtonLogin');
const modalLogin = document.querySelector('#modalLogin')

loginButton.addEventListener('click', () =>{
  modalLogin.showModal();

})

closeLoginButton.addEventListener('click', () =>{
  modalLogin.close();
})

function cadastrar() {
    var nomeCompleto = document.getElementById('nomeCompleto').value;
    var email = document.getElementById('email').value;
    var senha = document.getElementById('senha').value;
  
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
      window.location.href = '/';
    })
    .catch(error => {
      console.error('Erro ao cadastrar usuário:', error);
    });
  }
  
  document.getElementById('buttonCadastrar').addEventListener('click', cadastrar);