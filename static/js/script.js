document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('cambiarmodo');
    toggleButton.addEventListener('click', toggleModo);

    const savedMode = localStorage.getItem('mode');
    if (savedMode === 'dark') {
        toggleModo(); 
    }
});

function toggleModo() {
    const body = document.body;

    body.classList.toggle('light-mode');
    body.classList.toggle('dark-mode');

    const mode = body.classList.contains('light-mode') ? 'light' : 'dark';
    localStorage.setItem('mode', mode);

    if (mode === 'dark') {
        body.style.backgroundColor = '#132436';
        body.style.color = 'white'; 
    } else {
        body.style.backgroundColor = 'white';
        body.style.color = 'black'; 
    }

    const toggleButton = document.getElementById('cambiarmodo');
    const sunIcon = toggleButton.querySelector('.sun');
    const moonIcon = toggleButton.querySelector('.moon');
    if (mode === 'dark') {
        sunIcon.style.display = 'none';
        moonIcon.style.display = 'inline-block';
    } else {
        sunIcon.style.display = 'inline-block';
        moonIcon.style.display = 'none';
    }
}


function zoomSi(img) {
        img.classList.add('zoom');
    }

function zoomNo(img) {
        img.classList.remove('zoom');
    }

function expandirImagen(img) {
        var expandida = document.getElementById('imagenExpandida');
        var expandidaImg = document.getElementById('imagenExpandidaImg');
        expandidaImg.src = img.src;
        expandidaImg.alt = img.alt;
        expandida.style.display = 'flex';
    }

function cerrarImagen() {
        var expandida = document.getElementById('imagenExpandida');
        expandida.style.display = 'none';
    }
