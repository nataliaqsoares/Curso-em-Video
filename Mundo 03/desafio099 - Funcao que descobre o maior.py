""" Desafio 099
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa
tem que analisar todos os valores e dizer qual deles é o maior. Obs.: Informar quantos valores foram passados. Fazer
pequenas pausas entre a exibição dos resultados """

from time import sleep


def maior(*conj):
    maior2 = cont = 0
    print('Os números passados foram: ', end='')
    for num in conj:
        if num > maior2:
            maior2 = num
        cont += 1
        print(num, end=' ')
        sleep(1)
    print(f'\nForam informados {cont} números ao todo.\nO maior é o {maior2}.')
    print('-' * 40)


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
