// trazendo o prompt-sync para o projeto - npm i prompt-sync
const prompt = require('prompt-sync')()

function getUserInfo(){
    let altura = prompt("Digite sua altura")
    let peso = prompt("Digite seu peso")

    // console.log(altura,peso)
    return {
        pesoInfo: peso,
        alturaInfo: altura
        // mensagem: 'Olá',
    }
}

// console.log(getUserInfo())

function calcImc(alturaDoUsuario = 0, pesoDoUsuario = 0){
    return pesoDoUsuario / alturaDoUsuario **2
}

function main(){
    let peso = getUserInfo().pesoInfo
    let altura = getUserInfo().alturaInfo
    let imc = calcImc(altura,peso)
    console.log(`Seu IMC é ${imc === 24? 'Você está maromba': 'Não'}`)
}
main()