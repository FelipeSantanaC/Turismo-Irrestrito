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

    const headers = {
        'X-CSRFToken':getCookie('csrftoken'),
    }

    fetch(url, {
        method: 'POST',
        headers: headers,
    })
    .then(response => response.json())
    .then(data => {
        if (!data.success) {
            // Change the thing on the pop up

            $('#error-messages').empty();
            $.each(data.message, function (index, message) {
                let error_message = message.split(':')[1].trim();
                $('#error-messages').append('<p id="error-message">' + error_message +'</p>');
            })

            handleFormErrors(data.message)
            // failedRegister.innerText = "Email ou Senha invalido."
        } else {
            window.location.reload()
        }
    })
    
})

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function handleFormErrors(errors) {
    const formInputs = document.querySelectorAll('input');
    
    // Remove error styles from all inputs
    formInputs.forEach(input => {
      input.classList.remove('error-field');
    });
  
    // Update the form inputs with error styles
    for (const error of errors) {
      const field = error.split(':')[0].trim();
      const input = document.getElementById(`id_${field}`);
      if (input) {
        input.classList.add('error-field');
        if (field == 'password1') {
            const input = document.getElementById(`id_password2`);
            input.classList.add('error-field')
        }
      }
    }
  }
  