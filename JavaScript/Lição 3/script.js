function calcular() {
    const numero = parseInt(document.getElementById("numero").value);
    const resposta = document.getElementById("resposta");
    let resultado;

    if (document.getElementById("tempCelsiusFahrenheit").checked) {
        resultado = CelsiusParaFahrenheit(numero);
        resposta.textContent = `${numero}°C é igual a ${resultado}°F`;
    } else if (document.getElementById("tempFahrenheitCelsius").checked) {
        resultado = FahrenheitParaCelsius(numero);
        resposta.textContent = `${numero}°F é igual a ${resultado}°C`;
    } else {
        resposta.textContent = "Por favor, selecione um tipo de conversão.";
    }
}

function CelsiusParaFahrenheit(num) {
    return (1.8 * num + 32).toFixed(2);
}

function FahrenheitParaCelsius(num) {
    return ((num - 32) * 5/9).toFixed(2);
}

function limparCampos() {
    document.getElementById("numero").value = "";
    document.getElementById("resposta").textContent = "";
    console.log("Limpar Campos");
}
