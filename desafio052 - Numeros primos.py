""" Desafio 052
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. """

num = int(input('Digite o número que deseja saber se é primo: '))
cont = 0

for c in range(1, num+1):
    if num % c == 0:
        cont += 1
if cont == 2:
    print('O número {} é um número primo.'.format(num))
else:
    print('O número {} não é um número primo'.format(num))
