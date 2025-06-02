console.log("Hello, World!");

let mensagem1 = 'Inicio do Aprendizado'
let mensagem2 = 'da Linguagem JavaScript'
console.log(mensagem1);
console.log(mensagem2);

{
    let a = 0;
    var b = 0;
    
}

console.log(b);/*Vai funcionar, pois foi declarado como
                *VAR dentro de um bloco,
                *portanto é acessivel fora de escopo*/

let qualquer = "legal";
console.log(qualquer);
console.log(typeof qualquer);
qualquer = 3.1516;
console.log(qualquer);
console.log(typeof qualquer);
//evitar colocar nome genéricos e siglas
//let valor = 1
//let numero =1
//let pqp = false //produto químico perigoso


//declarando variáveis
let x = 10;
//numero inteiro
let y = 20;
//numero inteiro
let dolar =2.62;
//numero fracionado
let soma = 0;
//exibindo valores
console.log(x);
console.log();
console.log(y);
console.log();
console.log(dolar);
//somando números inteiros com número fracionado
soma = x+y+dolar;
//exibindo resultado
console.log('\n' + soma);



/* Crie um programa para calcular e apresentar o valor *do volume de uma lata de óleo, utilizando a fórmula:
*VOLUPIE 3.14159 RAIO-2 ALTURA*/
//criando variaveis
let volume= 0;
let raio =34.5;
let altura = 1.45;
const PI =3.14159;
//calculando
volume =PI*raio- 2* altura;
//exibindo resultado
//exibindo valor sem arredondamento
console.log("\n Exibindo valor sem arredondamento");
console.log("O volume e =" + volume);
console.log('\n Exihindo valor com arredondamento');
console.log("0 volume e =" + Math.floor(volume));