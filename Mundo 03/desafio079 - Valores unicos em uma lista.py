"""Desafio 079
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista la dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente
"""

valores = list()

while True:
    num = int(input('Digite um número: '))
    if num not in valores:
        valores.append(num)
        print('Número adicionado com sucesso.')
    else:
        print('Esse número já foi adicionado anteriormente.')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break

valores.sort()
print(f'Foram digitados os seguintes números: {valores}')
