""" Desafio 054
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
maioridade e quantas já são maiores. Considerar a maioridade com 21 anos """

from datetime import date

maior = 0
menor = 0

for c in range(0, 7):
    ano = int(input('Digite seu ano de nascimento: '))
    if date.today().year - ano >= 21:
        maior += 1
    else:
        menor += 1

print('Das 7 pessoas, {} são maiores de idade e {} são menores de idade'.format(maior, menor))
