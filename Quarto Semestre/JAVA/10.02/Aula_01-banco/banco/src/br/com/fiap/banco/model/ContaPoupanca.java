package br.com.fiap.banco.model;

public class ContaPoupanca extends Conta {
	
	private double rendimento;
	
	public ContaPoupanca(int agencia, int conta, double rendimento) {
		this.agencia = agencia;
		this.conta = conta;
		this.rendimento = rendimento;
	}

	public double getRendimento() {
		return rendimento;
	}

	public void setRendimento(double rendimento) {
		this.rendimento = rendimento;
	}

	@Override
	public void sacar(double valor) {
		System.out.println("Saque no valor de R$ " + valor + " da Conta Poupança.");
		this.saldo -= valor;
		
	}

	@Override
	public void depositar(double valor) {
		System.out.println("Depósito no valor de R$ " + valor + " da Conta Poupança.");
		this.saldo += valor;
		
	}

	@Override
	public void exibirSaldo() {
		System.out.println("O saldo da sua Conta Poupança é R$ " + this.saldo );
	}
}
