// Definindo a velocidade média e o tempo gasto na viagem
const velocidadeMedia = 80; // km/h
const tempoGasto = 2; // horas

// Calculando a distância percorrida
const distanciaPercorrida = velocidadeMedia * tempoGasto;

// Calculando a quantidade de litros de combustíveL utilizada
const litrosUtilizados = distanciaPercorrida / 12;

// Apresentando os resultados
console.log('Velocidade média:'+velocidadeMedia, 'km/h')
console.log('Tempo gasto na viagem:' +tempoGasto,' horas')
console.log('Distância percorrida: '+distanciaPercorrida,' km')
console.log('Litros de combustíveL utilizados:'+litrosUtilizados.toFixed(2), 'L')
