""" Desafio 035
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

reta1 = float(input('Informe o valor da primeira reta:'))
reta2 = float(input('Informe o valor da segunda reta:'))
reta3 = float(input('Informe o valor da terceira reta:'))

if (reta2 - reta3) < reta1 < reta2 + reta3 and (reta1 - reta3) < reta2 < reta1 + reta3 and (reta1 - reta2) < reta3 < \
        reta1 + reta2:
    print('Essas retas podem forma um triângulo')
else:
    print('Essas retas não podem formam um triângulo')
