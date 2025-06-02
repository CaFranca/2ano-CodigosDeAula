for (let i = 0; i < 5; i++) {
    if (i === 2) {
      continue; // Pula a iteração quando i é igual a 2
    }
    console.log(i);
  }
  
  // Saída:
  // 0
  // 1
  // 3
  // 4
  