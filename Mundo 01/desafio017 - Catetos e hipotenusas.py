""" Desafio 017
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
mostre o comprimento da hipotenusa. """

# Solução 1
import math
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
hipo = math.hypot(co, ca)
print('Com os catetos {} e {} temos a hipotenusa de {}'.format(co, ca, hipo))

# Solução 2
from math import hypot
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
hipo = hypot(co, ca)
print('Com os catetos {} e {} temos a hipotenusa de {}'.format(co, ca, hipo))

# Soluação 3
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
hipo = (co ** 2 + ca ** 2) ** (1/2)
print('Com os catetos {} e {} temos a hipotenusa de {}'.format(co, ca, hipo))
