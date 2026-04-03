document.addEventListener("DOMContentLoaded", function () {
  
  const form = document.querySelector("form");

  form.addEventListener("submit", function (event) {
    
    const peso = document.querySelector("input[name='peso']").value;
    const altura = document.querySelector("input[name='altura']").value;

    if (!peso || !altura) {
      event.preventDefault(); // impede o envio
      alert("Preencha todos os campos!");
      return;
    }

    if (peso <= 0 || altura <= 0) {
      event.preventDefault();
      alert("Valores devem ser maiores que zero!");
      return;
    }

  });

});