""" Desafio 098
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a
contagem. Seu programa tem que realizar três contagens através da função criada: a) De 1 até 10, de 1 em 1; b) De 10 até
0, de 2 em 2; c) Uma contagem personalizada. Obs.: Se o passo for negativo, passar para positivo; Se o passo for 0,
trocar para 1 """

from time import sleep


def contador(i, f, p):
    cont = 0
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-' * 45)
    print(f'Contagem de {i} até {f} de {p} em {p}\n{i} ', end='')
    while True:
        if i < f:
            cont = i + p
            if cont == f:
                print(cont, 'FIM!')
                break
            if cont > f:
                print('FIM!')
                break
            print(cont, end=' ')
            sleep(1)
            i = cont
        if i > f:
            cont = i - p
            if cont == f:
                print(cont, 'FIM!')
                break
            if cont < f:
                print('FIM')
                break
            print(cont, end=' ')
            sleep(1)
            i = cont
    print('-' * 45)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
