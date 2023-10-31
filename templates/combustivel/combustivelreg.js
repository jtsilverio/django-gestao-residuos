const data = document.getElementById("data");
const litros = document.getElementById("litros");
const form = document.querySelector("form");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const registro = {
    data: data.value,
    litros: litros.value,
  };

  // Salvar o registro no banco de dados.

  // Limpar o formulário.

  data.value = "";
  litros.value = "";
});