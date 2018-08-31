"""Desafio 014
Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF"""

c = int(input('Informe a temperatura: '))
f = 1.8 * c + 32
print('{}ºC são {}ºF'.format(c, f))
