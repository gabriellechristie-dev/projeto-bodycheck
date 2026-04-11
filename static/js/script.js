document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");

  form.addEventListener("submit", function (event) {
    const peso = parseFloat(document.querySelector("input[name='peso']").value);
    const altura = parseFloat(document.querySelector("input[name='altura']").value);

    if (!peso || !altura) {
      event.preventDefault();
      alert("Preencha todos os campos!");
      return;
    }

    if (peso <= 0 || altura <= 0) {
      event.preventDefault();
      alert("Valores devem ser maiores que zero!");
      return;
    }

    if (altura > 3) {
      // aviso leve, não bloqueia
      alert("Altura acima de 3m detectada. Verifique se está em cm.");
    }
  });
});