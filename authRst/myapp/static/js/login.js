const confirmButton = document.getElementById('confirm-login-button');
const failedLogin = document.getElementById('login-message');

confirmButton.addEventListener('click', function() {
    const form = document.getElementById('login-form');
    const formData = new FormData(form)

    const email = formData.get('email');
    const password = formData.get('password1');


    const url = `/user_login/?email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`
    const dataToSend = {
        email:email,
        password1:password
    };

    fetch(url, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(data => {
        if (!data.success) {
            // Change the thing on the pop up
            failedLogin.innerText = "Email ou Senha invalido."
        } else {
            console.log(data)
            window.location.href = data.redirect_url;
        }
    })
    
})
