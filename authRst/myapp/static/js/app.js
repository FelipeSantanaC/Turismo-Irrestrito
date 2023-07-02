const registerButton = document.querySelector('#register-button');
const closeRegisterButton = document.querySelector('#closeButtonCadastro');
const modal = document.querySelector('#modalCadastro')

registerButton.addEventListener('click', () =>{
    modal.showModal();

})

closeRegisterButton.addEventListener('click', () =>{
    modal.close();
})