""" Desafio 096
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
comprimento) e mostre a área do terreno. """


def area(a, b):
    areas = a * b
    print(f'A área de um terreno de {a} x {b} é de {areas}m³.')


# Programa Principal
larg = float(input('Informe a largura do terreno (m): '))
comp = float(input('Informe o comprimento do terreno (m): '))

area(larg, comp)
