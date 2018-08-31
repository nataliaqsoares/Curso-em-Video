"""Desafio 012
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto"""

preco = float(input('Informe o preço do produto: '))
novopreco = preco - (preco * 0.05)
print('O produto de preço {} com desconto fica por {:.2f}'.format(preco, novopreco))
