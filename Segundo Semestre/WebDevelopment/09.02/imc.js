// Calcular o IMC

const prompt = require("prompt-sync")()
function calcularIMC(peso, altura) {
   return peso / (altura * altura);
}

function interpretarIMC(imc) {
   if (imc < 18.5) {
       return "Abaixo do peso";
   } else if (imc >= 18.5 && imc < 24.99) {
       return "Normal";
   } else if (imc >= 25 && imc < 29.99) {
       return "Sobrepeso";
   } else {
       return "Obesidade";
   }
}

const peso = prompt("Digite seu peso"); 
const altura = prompt("Digite sua altura"); 
const imc = calcularIMC(peso, altura);
console.log("Seu IMC é:", imc.toFixed(2));
console.log("Você está:", interpretarIMC(imc));

// como rodar código no terminal
// npm -y
// npm i prompt-sync
// node imc.js