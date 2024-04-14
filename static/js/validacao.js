function validarTexto(campoId) {
  var campoTexto = document.getElementById(campoId);
  var mensagemErro = document.getElementById("mensagemErro" + campoId.charAt(campoId.length - 1));

  // Expressão regular para permitir apenas letras, números, traços e subtraços
  var regex = /[^\w-]/g;

  if (regex.test(campoTexto.value)) { 
    mensagemErro.textContent = "Use apenas letras, números, traços e subtraços.";
    campoTexto.setCustomValidity("Use apenas letras, números, traços e subtraços.");
  } else {
    mensagemErro.textContent = "";
    campoTexto.setCustomValidity("");
  }
}

document.getElementById("meuFormulario").addEventListener("submit", function (event) {
  // Impede o envio do formulário se houver erros de validação
  if (!this.checkValidity()) {
    event.preventDefault();
  }
});