
let step = 1;
let allsteps = 1;
document.addEventListener('DOMContentLoaded', () => {

  const registerButton = document.getElementById("register-button");
  const loginButton = document.getElementById("login-button");
  const registerButtonBoot = document.getElementById("register-button-boot");
  const loginButtonBoot = document.getElementById("login-button-boot");

  registerButton.addEventListener("click", () => {
    openPopup('/popup/?model=0', 0)
  });
  registerButtonBoot.addEventListener("click", () => {
    openPopup('/popup/?model=0', 0)
  });

  loginButton.addEventListener("click", () => {
    openPopup('/popup/?model=1', 1)
  });

  loginButtonBoot.addEventListener("click", () => {
    openPopup('/popup/?model=1', 1)
  });
})

function openPopup(url, typePopup=undefined) {
  // Make an AJAX request to the provided URL
  fetch(url)
    .then(response => response.text())
    .then(data => {
        // Inject the pop-up content into the DOM
        const popupContainer = document.createElement('popup');
        const overlay = document.createElement('div');

        popupContainer.classList.add('popup-container')
        overlay.classList.add('overlay')
        popupContainer.innerHTML = data;
        document.body.appendChild(popupContainer);
        document.body.appendChild(overlay);
        document.addEventListener('wheel', preventScroll, { passive: false }); // Prevent scroll

        // To "upload" the js file into the base.html 
        // login == 1 | register == 0
        const scriptElement = document.createElement('script');
        if (typePopup == 1) {
          // this is to load the login.js into the page
          scriptElement.src = '../static/js/login.js';
        } else if (typePopup == 0) {
          scriptElement.src = '../static/js/register.js';
        }
        document.body.appendChild(scriptElement);

        // Close button functionality
        const closeButton = document.getElementById('close-button');
        closeButton.addEventListener('click', () => {
          document.body.removeChild(popupContainer);
          document.body.removeChild(overlay);
          document.body.removeChild(scriptElement)
          document.removeEventListener('wheel', preventScroll); // Prevent scroll
          step = 1;
        });
        

    }).then(() => {
      const previousButtonWizard = document.getElementById('previous-button-wizard');
      const nextButtonWizard = document.getElementById('next-button-wizard');
      const wizardContent = document.querySelector('.wizard-content');
      try {
        const userType = wizardContent.getAttribute('data-value');
        nextButtonWizard.addEventListener('click', () => {getNextStep(userType)})
        previousButtonWizard.addEventListener('click', () => {previousPopUpStep()})
      } catch (error) {}

    });
}

function getNextStep(userType) {
  const wizard = document.querySelector('.wizard-content');
  const howManySteps = wizard.children.length;
  
  if (step != howManySteps) {
    const steps = wizard.children;
    steps[step].classList.remove('disable-wizard') // Show the current step
    steps[step-1].classList.add('disable-wizard') // Hide other steps

    const previousButton = document.querySelector('#previous-button-wizard');
    previousButton.disabled = false;
    step++;
  } else {
    fetch(`nextWizard/?step=${step+1}&pcd=${userType}`)
    .then(response => response.text())
    .then(data => {
      const newElement = document.createElement('div');
      newElement.classList.add('step')
      
      const previousButton = document.querySelector('#previous-button-wizard');
      previousButton.disabled = false;
      
      newElement.innerHTML = data;
      
      const existingChildren = wizard.children;
      
      for (let i = 0; i < existingChildren.length; i++) {
        existingChildren[i].classList.add('disable-wizard') // Hide other steps
      }
      
      step++;
      allsteps++;
      
      wizard.appendChild(newElement);
    })
  }
  
}

function previousPopUpStep() {
  const wizard = document.querySelector('.wizard-content');
  
  const steps = wizard.children;
  
  steps[step-1].classList.add('disable-wizard')
  step--;
  steps[step-1].classList.remove('disable-wizard')
  
  const previousButton = document.querySelector('#previous-button-wizard')
  if (step === 1) {
    previousButton.disabled = true
  }
}

function preventScroll(event) {
  // Prevent scroll on the underlying content
  event.preventDefault();
}


function ValidateEmail(mail) {
  if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail)) {
    return true;
  }
  alert("Você esta inserindo email inválido!");
  return false;
}

function cadastrar() {
  var nomeCompleto = document.getElementById("nomeCompleto").value;
  var email = document.getElementById("email").value;
  var senha = document.getElementById("senha").value;

  if (!ValidateEmail(email)) {
    return false;
  } else {
    var userData = {
      name: nomeCompleto,
      email: email,
      password: senha,
    };

    // Envia uma solicitação POST para a API do Django
    fetch("/api/myapp/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userData),
    })
      .then((response) => response.json())
      .then((data) => {
        window.location.href = "/";
      })
      .catch((error) => {
        console.error("Erro ao cadastrar usuário:", error);
      });
  }
}
