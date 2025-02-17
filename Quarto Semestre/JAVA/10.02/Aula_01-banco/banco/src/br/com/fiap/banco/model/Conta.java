package br.com.fiap.banco.model;

public abstract class Conta {
	
	protected int agencia;
	
	protected int conta;
	
	protected double saldo;
	
	public abstract void sacar(double valor);
	
	public abstract void depositar(double valor);
	
	public abstract void exibirSaldo();
	
	public int getAgencia() {
		return agencia;
	}

	public void setAgencia(int agencia) {
		this.agencia = agencia;
	}

	public int getConta() {
		return conta;
	}

	public void setConta(int conta) {
		this.conta = conta;
	}

	public double getSaldo() {
		return saldo;
	}
	
}
