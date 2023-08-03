const confirmButton = document.getElementById('confirm-register-button');
const failedRegister = document.getElementById('register-error-message');

confirmButton.addEventListener('click', function() {
    const form = document.getElementById('register-form');
    const formData = new FormData(form)

    const name = formData.get('name');
    const email = formData.get('email');
    const password1 = formData.get('password1');
    const password2 = formData.get('password2');


    const url = `/user_register/?name=${encodeURIComponent(name)}&email=${encodeURIComponent(email)}&password1=${encodeURIComponent(password1)}&password2=${encodeURIComponent(password2)}`;

    const dataToSend = {
        name: name,
        email: email,
        password1: password1,
        password2: password2
    };
    const hedaers = {
        'X-CSRFToken':getCookie('csrftoken'),
    }

    fetch(url, {
        method: 'POST',
        headers: headers,
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)  // Moises
        if (!data.success) {
            // Change the thing on the pop up
            failedRegister.innerText = "Email ou Senha invalido."
        } else {
            console.log(data)
            window.location.href = data.redirect_url;
        }
    })
    
})

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}