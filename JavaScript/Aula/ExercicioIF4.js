
var prova1 = 7;
var prova2 = 6;
var tr = 2; 
var faltas = 20; 


var media = ((prova1 * 0.4) + (prova2 * 0.6)) * 0.7 + tr;


if (media >= 6 && faltas < 24) {
    console.log("Aprovado");
} else if (media >= 3 && media < 6 && faltas < 24) {
    console.log("Exame");
} else {
    console.log("Reprovado");
    if (faltas >= 24) {
        console.log("Reprovado por faltas");
    }
}
