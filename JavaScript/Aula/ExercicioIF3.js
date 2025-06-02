
var salario = 700; 


var salarioReajustado;
if (salario < 500) {
    salarioReajustado = salario * 1.15; 
} else if (salario <= 1000) {
    salarioReajustado = salario * 1.10; 
} else {
    salarioReajustado = salario * 1.05; 
}


console.log("Salário antigo:", salario);
console.log("Salário reajustado:", salarioReajustado);
