
document.addEventListener('DOMContentLoaded', () => {
    idbutton = document.getElementById('make-review-button')

    idbutton.addEventListener('click', () => {
        openPopup('/popup/?model=4')
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
                scriptElement.src = '../static/js/make_review.js';
                
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
                    
    
        });
    }
})


