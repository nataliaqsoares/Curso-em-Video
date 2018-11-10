"""Desafio 014
Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF"""

c = float(input('Informe a temperatura ºC: '))
f = 1.8 * c + 32
print('{}ºC são {}ºF'.format(c, f))
