""" Desafio 015
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado """

km = float(input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias o carro ficou alugado? '))
total = (60 * dias) + (km * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(total))
