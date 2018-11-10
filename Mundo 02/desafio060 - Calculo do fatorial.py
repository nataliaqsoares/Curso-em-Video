""" Desafio 060
Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex.: 5! = 5x4x3x2x1=120. Fazer com while e for """

# Solução 1: Usando while

n = int(input('Informe um número: '))

num = n
fat = 1

while n != 1:
    fat *= n
    n -= 1

print('O fatorial de {}! é {}'.format(num, fat))

# Solução 2: Usando for

n = int(input('Informe um número: '))
fat = 1

for c in range(n, 1, -1):
    fat *= c
print('O fatorial de {}! é {}'.format(n, fat))

# Solução 3: Usando modulo, disponibilidado pelo Curso em Video

from math import factorial

n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))
