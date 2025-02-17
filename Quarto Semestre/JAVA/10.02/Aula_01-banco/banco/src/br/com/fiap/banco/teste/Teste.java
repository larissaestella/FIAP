package br.com.fiap.banco.teste;

import br.com.fiap.banco.model.ContaCorrente;
import br.com.fiap.banco.model.ContaPoupanca;

public class Teste {

	public static void main(String[] args) {

		ContaCorrente contaCorrente = new ContaCorrente(1000, 500, 20);
		contaCorrente.depositar(200);
		contaCorrente.exibirSaldo();
		contaCorrente.sacar(30);
		contaCorrente.sacar(20, "PIX");
		contaCorrente.exibirSaldo();
		
		ContaPoupanca contaPoupanca = new ContaPoupanca(2000, 1000, 30);
		contaPoupanca.depositar(150);
		contaPoupanca.exibirSaldo();
		contaPoupanca.sacar(30);
		contaPoupanca.exibirSaldo();


	}

}
