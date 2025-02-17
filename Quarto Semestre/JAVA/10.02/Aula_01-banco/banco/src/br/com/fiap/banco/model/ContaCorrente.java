package br.com.fiap.banco.model;

public class ContaCorrente extends Conta {
	
	private double limite;
	
	public ContaCorrente(int agencia, int conta, double limite) {
		this.agencia = agencia;
		this.conta = conta;
		this.limite = limite;
	}

	public double getLimite() {
		return limite;
	}

	public void setLimite(double limite) {
		this.limite = limite;
	}

	@Override
	public void sacar(double valor) {
		System.out.println("Saque no valor de R$ " + valor + " da Conta Corrente.");
		this.saldo -= valor;
		
	}
	
	public void sacar(double valor, String tipoSaque) {
		System.out.println("Saque no valor de R$ " + valor + " da Conta Corrente.");
		this.saldo -= valor;
		
	}
	
	public void sacar(double valor, double limite) {
		System.out.println("Saque no valor de R$ " + valor + " da Conta Corrente.");
		this.saldo -= valor;
		
	}
	
	@Override
	public void depositar(double valor) {
		System.out.println("Depósito no valor de R$ " + valor + " da Conta Corrente.");
		this.saldo += valor;
		
	}

	@Override
	public void exibirSaldo() {
		System.out.println("O saldo da sua Conta Corrente é R$ " + this.saldo );
	}
	

}
