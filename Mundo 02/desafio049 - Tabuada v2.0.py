""" Desaio 049
Refaça o Desafio 009, mostre a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""

n = int(input('Digite o número da tabuada que deseja: '))
for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, n * c))
