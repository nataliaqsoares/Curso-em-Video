"""Desafio 018
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo"""

# Solução 1
import math
angulo = float(input('Informe o ângulo: '))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cos = math.cos(radiano)
tang = math.tan(radiano)
print('O ângulo {} em radiano é {} tem o seno de {}, cosseno de {} e a tangente de {}'
      .format(angulo, radiano, seno, cos, tang))

# Solução 2
from math import radians, sin, cos, tan
angulo = float(input('Informe o ângulo: '))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tang = tan(radians(angulo))
print('O ângulo {} tem o seno de {}, cosseno de {} e tangente de {}'.format(angulo, seno, cos, tang))

# Solução 3 - Fazer sem o uso de módulos
