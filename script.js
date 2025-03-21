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

//function changeImage(imageSrc) {
//    document.getElementById("mainImage").src = imageSrc;
//}

function changeImage(imageName, imageSrc) {
    // Hitta bilden med det angivna namnet
    var image = document.querySelector(`img[id='${imageName}']`);
    
    if (image) {
        // Om bilden finns, ändra dess src
        image.src = imageSrc;
    } else {
        //console.log("Bild med namn " + imageName + " hittades inte.");
    }
}





window.addEventListener('DOMContentLoaded', function() {
    // Hämta alla bilder med class="images_table"
    const images = document.querySelectorAll('.images_table');
    
    // Kontrollera om bilderna finns
    if (images.length === 0) {
        console.log('Inga bilder med class "images_table" hittades!');
        return;
    }
    
    // Referens till tabellen för att lägga till miniatyrbilder
    const thumbnailTable = document.getElementById('thumbnailTable');
    
    // Skapa en rad för tabellen
    let row;

    // För varje bild på sidan, skapa en miniatyrbild och en länk
    images.forEach((image, index) => {
        // Skapa en ny rad för tabellen var tredje bild
        if (index % 3 === 0) {
            // Skapa en ny rad för varje uppsättning av 3 bilder
            row = document.createElement('tr');
            thumbnailTable.appendChild(row);
        }

        // Skapa en cell i tabellen
        var cell = document.createElement('td');
        
        // Skapa länk till den stora bilden (refererar till bildens id)
        var link = document.createElement('a');
        link.href = `#${image.id}`;  // Länk till den aktuella bildens id
        link.title = `Se Bild ${index + 1}`; // Tooltip på länken
        
        // Skapa miniatyrbilden
        var thumbnail = document.createElement('img');
        thumbnail.src = image.src; // Använd samma bildkälla för miniatyr
        thumbnail.alt = `Thumbnail ${index + 1}`;
        thumbnail.classList.add('thumbnail');
        
        // Lägg till miniatyrbilden i länken, och länken i cellen
        link.appendChild(thumbnail);
        cell.appendChild(link);
        
        // Lägg till cellen i den aktuella raden
        row.appendChild(cell);
    });

    // Lägg till en event listener för länkarna
    const links = document.querySelectorAll('a[href^="#"]'); // Hämta alla länkar som börjar med #

    links.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // Förhindra standardbeteendet för länken

            // Hämta elementet som är målet för länken
            const targetId = link.getAttribute('href').substring(1); // Ta bort '#' från href
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                // Använd scrollIntoView för att rulla till målbilden
                targetElement.scrollIntoView({
                    behavior: 'smooth', // Gör rullningen mjuk
                    block: 'center'     // Centrera bilden vertikalt i fönstret
                });

                // Omedelbart efter scrollning, justera scrollTop för att flytta sidan längre ner
                window.scrollBy(0, -100); // Scrolla lite längre ner (eller upp), justera värdet
            }
        });
    });





});
