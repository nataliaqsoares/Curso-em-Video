""" Desafio 084
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: a) Quantas
pessoas foram cadastradas b) uma listagem com as pessoas mais pesadas c) uma listagem com as pessoas mais leves. """

pessoas = list()
dados = list()
pesoleve = pesopesado = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        pesoleve = pesopesado = dados[1]
    else:
        if dados[1] > pesopesado:
            pesopesado = dados[1]
        elif dados[1] < pesoleve:
            pesoleve = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? ')).strip().lower()[0]
    if continuar == 'n':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas\nO maior peso foi de {pesopesado}Kg de ', end='')
for dado in pessoas:
    if dado[1] == pesopesado:
        print(dado[0], end=', ')

print(f'\nO menor peso foi de {pesoleve}Kg de ', end='')
for dado in pessoas:
    if dado[1] == pesoleve:
        print(dado[0], end=', ')
