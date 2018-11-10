""" Desafio 016
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
Ex: Digite um numero: 6.127. O número 6.127 tem a parte inteira 6. """

# Solução 1
import math
num = float(input('Informe um número real qualquer: '))
int = math.trunc(num)
print('O número {} tem a porção inteira de {}'.format(num, int))

# Solução 2
from math import trunc
num = float(input('Informe um número real qualquer: '))
int = trunc(num)
print('O número {} tem a porção inteira de {}'.format(num, int))

# Solução 3
num = float(input('Informe um núemro real qualquer: '))
print('O número {} tem a porção interira de {:.0f}'.format(num, num // 1))

# Solução 4
num = float(input('Informe um número real qualquer: '))
print('O número {} tema a porção interira de {}'.format(num, int(num)))
