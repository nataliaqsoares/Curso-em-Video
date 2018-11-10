""" Desafio 051
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão """

inicio = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão para essa progressão: '))

fim = inicio + (11 - 1) * razao
contador = 1

for c in range(inicio, fim, razao):
    print('{}º termo: {}'.format(contador, c))
    contador += 1
