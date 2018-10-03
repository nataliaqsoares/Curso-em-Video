""" Desafio 074
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla. """

from random import randint
maior = menor = 0
n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)
conjunto = (n1, n2, n3, n4, n5)
print(f'Os números sorteados foram: ', end='')
for pos, num in enumerate(conjunto):
    print(num, end=' ')
    if pos == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f'\nO maior número sorteado foi: {maior}\nO menor número sorteado foi: {menor}')
