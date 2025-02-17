package br.com.fiap.rh.teste;

import java.util.ArrayList;
import java.util.List;

import br.com.fiap.rh.model.Endereco;
import br.com.fiap.rh.model.Pessoa;

public class TesteLista {

	public static void main(String[] args) {
		
		List<String> lista = new ArrayList<String>();
		lista.add("Teste 1");
		lista.add("Teste 2");
		
		for(String texto : lista) {
			System.out.println(texto);
		}
		
		Pessoa pessoa1 = new Pessoa("Larissa", "11122233344", 20);
		Pessoa pessoa2 = new Pessoa("Estella", "11122233344", 22);
		
		List<Pessoa> pessoas = new ArrayList<>();
		pessoas.add(pessoa1);
		pessoas.add(pessoa2);
		
		for(Pessoa pessoa : pessoas) {
			pessoa.imprimir();
		}
		
		for(int i = 0; i < 5; i++) {
			Pessoa pessoa = new Pessoa("Teste" + i, i+i+""+i+i+i, i);
			pessoa.imprimir();
			pessoas.add(pessoa);
		}
		
		Endereco endereco1 = new Endereco("Rua tal", 20, "22222");
		Endereco endereco2 = new Endereco("Aquela rua", 22, "00000");
		
		List<Endereco> enderecos = new ArrayList<>();
		enderecos.add(endereco1);
		enderecos.add(endereco2);
		
		for(Endereco endereco : enderecos) {
			endereco.imprimir();
		}
		
		//*for (int i = 0; i<lista.size();i++) {
			
		//*}

	}

}
