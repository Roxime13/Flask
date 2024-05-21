"use strict";

var toggleButton = document.getElementById('toggle-mode');
var body = document.body; // Escucha el evento de clic en el botón

toggleButton.addEventListener('click', function () {
  // Alterna entre los modos claro y oscuro
  body.classList.toggle('light-mode');
  body.classList.toggle('dark-mode');
});