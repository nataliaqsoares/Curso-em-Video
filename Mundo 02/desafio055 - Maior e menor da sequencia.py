""" Desafio 055
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos. """

peso = float(input('Informe o seu peso: '))
menor = peso
maior = peso

for c in range(0, 4):
    peso = float(input('Informe o seu peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('Maior peso: {}Kg\nMenor peso: {}Kg'.format(maior, menor))
