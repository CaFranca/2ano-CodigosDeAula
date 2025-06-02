function calcularAnos() {
    // Obtém os valores dos campos do formulário
    const popA = parseFloat(document.getElementById('popA').value);
    const taxaA = parseFloat(document.getElementById('taxaA').value) / 100;
    const popB = parseFloat(document.getElementById('popB').value);
    const taxaB = parseFloat(document.getElementById('taxaB').value) / 100;

    // Valida os valores inseridos
    if (isNaN(popA) || isNaN(taxaA) || isNaN(popB) || isNaN(taxaB)) {
        alert('Por favor, preencha todos os campos com números válidos.');
        return;
    }

    let anos = 0;
    while (popA <= popB) {
        popA += popA * taxaA;
        popB += popB * taxaB;
        anos++;
    }

    // Exibe o resultado na div com id "resultado"
    document.getElementById('resultado').innerHTML = `O país A ultrapassará o país B em ${anos} anos.`;
}

function limparCampos() {
    // Limpa todos os campos do formulário
    document.getElementById('formCalculo').reset();
    document.getElementById('resultado').innerHTML = '';
}
