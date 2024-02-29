function dados(){
    let numLivros = Number(prompt("Qual a quantidade de livros que você vai comprar?"))
    return numLivros
}

function precoLivro(numLivros){

    if (numLivros >=7){
        return numLivros * 15
    } else {
        return numLivros * 22
    }
}

function main(){

}