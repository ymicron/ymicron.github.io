// Hämta referenser till element
const languageBtn = document.getElementById('language-btn');
const dropdownMenu = document.getElementById('language-dropdown').querySelector('.dropdown-menu');

// Lägg till en event listener på språkknappen för att växla synligheten på menyn
languageBtn.addEventListener('click', function(event) {
    event.preventDefault(); // Förhindra att knappen gör något annat, t.ex. ladda om sidan
    
    // Växla synligheten på menyn
    dropdownMenu.style.display = (dropdownMenu.style.display === 'block') ? 'none' : 'block';
});

// Stäng dropdown menyn om användaren klickar utanför
window.addEventListener('click', function(event) {
    if (!languageBtn.contains(event.target) && !dropdownMenu.contains(event.target)) {
        dropdownMenu.style.display = 'none'; // Stänger menyn om man klickar utanför
    }
});

function changeImage(imageSrc) {
    document.getElementById("mainImage").src = imageSrc;
}
