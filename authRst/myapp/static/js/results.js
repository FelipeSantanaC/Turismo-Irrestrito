
// Checkbox handle
function addCheckboxFunctionality() {
  const checkboxes = document.getElementsByClassName('checkbox-label')

  for (let i = 0; i < checkboxes.length; i++) {
    const checkbox = checkboxes[i].querySelector('input[type="checkbox"]');
    if (checkbox.checked) {
      checkbox.parentNode.classList.add('checked')
    }
    
    checkbox.addEventListener('change', () => {
      if (checkbox.checked) {
        checkbox.parentNode.classList.add('checked')
        // Submit 
      } else {
        checkbox.parentNode.classList.remove('checked')
      }
      updateCardSelect()
    })
  }
}


// Create a function to retrieve the text from input and send to the function bellow 

document.addEventListener('DOMContentLoaded', () => {
  const submitSearch = document.getElementById('search-form');
  
  submitSearch.addEventListener('submit', event => {

    event.preventDefault();
  
    updateCardSelect()
  })
})


function updateCardSelect(checkboxes=undefined) {
  let selected = []
  if (checkboxes == undefined) {
    const checkboxes = document.getElementsByClassName('checkbox-label')

    for (let i = 0; i < checkboxes.length; i++) {
      const checkbox = checkboxes[i].querySelector('input[type="checkbox"]');

      if (checkbox.checked) {
        selected.push(checkbox.value)
      }
    }
  }
  const searchInput = document.getElementById('input-local').value
  let queryParams = ''
  if (searchInput.length == 0 && selected == 0) {
    queryParams = new URLSearchParams({
      checkboxesData: 'all', // Convert the selected array to a comma-separated string
      searchQuery: 'all',
    });

  } else {
    queryParams = new URLSearchParams({
      checkboxesData: selected.join(','), // Convert the selected array to a comma-separated string
      searchQuery: searchInput,
    });
  }
  const url = '/results/?' + queryParams;



  fetch(url, {
    method:'GET',
    })
  .then(response => response.json())
  .then(data => {

    // Get the parent container that wraps the card-container div
    const parentContainer = document.getElementById('parent-container');

    // Create a new div to hold the updated content
    const updatedCardContainer = document.createElement('div');
    updatedCardContainer.className = 'card-container';
    updatedCardContainer.id = 'card-container';

    // Loop through the data and update the content of the updatedCardContainer
    data.data.forEach(local => {
      // Create a new div for each local
      const cardDiv = document.createElement('div');
      cardDiv.className = 'card';
      cardDiv.style.backgroundColor = '#558BE2';

      // Create the image overlay
      const imageOverlay = document.createElement('div');
      imageOverlay.className = 'image-overlay';

      // Check if local has a photo URL, otherwise display a default image
      const imageUrl = local.foto_url ? local.foto_url : '../static/images/img-not-found.png';
      const image = document.createElement('img');
      image.className = 'card-image';
      image.src = imageUrl;
      image.alt = local.nome;

      // Overlay content
      const overlayContent = document.createElement('div');
      overlayContent.className = 'overlay-content';
      const nameHeader = document.createElement('h3');
      nameHeader.id = 'local-name-card';
      nameHeader.textContent = local.nome;
      const neighborhood = document.createElement('p');
      neighborhood.id = 'local-neighborhood-card';
      neighborhood.textContent = local.bairro;

      overlayContent.appendChild(nameHeader);
      overlayContent.appendChild(neighborhood);

      // Append the image and overlay content to the image overlay
      imageOverlay.appendChild(image);
      imageOverlay.appendChild(overlayContent);

      // Append the image overlay to the card div
      cardDiv.appendChild(imageOverlay);

      // Card body
      const cardBody = document.createElement('div');
      cardBody.id = 'card-body';
      const numReviews = document.createElement('p');
      numReviews.textContent = local.relevancia + ' Avaliações';
      const starRating = document.createElement('div');
      starRating.className = 'star-rating';
      const rating = document.createElement('p');
      rating.textContent = local.nota;

      starRating.appendChild(rating);

      // Append the card body to the card div
      cardBody.appendChild(numReviews);
      cardBody.appendChild(starRating);
      cardDiv.appendChild(cardBody);

      // Append the cardDiv to the updatedCardContainer
      updatedCardContainer.appendChild(cardDiv);
    });

    // Replace the existing card-container div with the updated content
    parentContainer.replaceChild(updatedCardContainer, document.getElementById('card-container'));
  })
  .catch(error => {
    console.error('Error occurred during AJAX request:', error);
  });
}  
