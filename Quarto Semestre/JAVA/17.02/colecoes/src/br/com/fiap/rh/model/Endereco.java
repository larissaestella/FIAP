package br.com.fiap.rh.model;

import java.util.List;

public class Endereco {

	private String rua;
	
	private int numero;
	
	private String cep;
	
	private List<Endereco> enderecos;

	public Endereco(String rua, int numero, String cep) {
		this.rua = rua;
		this.numero = numero;
		this.cep = cep;
	}
	
	public void imprimir() {
		System.out.println("O endereco da pessoa e: " + this.rua + ", numero: " + this.numero + " e o cep e: " + this.cep);
	}

	public String getRua() {
		return rua;
	}

	public void setRua(String rua) {
		this.rua = rua;
	}

	public int getNumero() {
		return numero;
	}

	public void setNumero(int numero) {
		this.numero = numero;
	}

	public String getCep() {
		return cep;
	}

	public void setCep(String cep) {
		this.cep = cep;
	}
	
	public List<Endereco> getEnderecos() {
		return enderecos;
	}

	public void setEnderecos(List<Endereco> enderecos) {
		this.enderecos = enderecos;
	}
	
	
}
