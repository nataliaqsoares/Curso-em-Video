""" Desafio 100
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior """

from random import randint
from time import sleep


def sorteia(lst):
    print('Sorteando os 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        lst.append(n)
        print(n, end=' ')
        sleep(1)
    print('Pronto!')


def somaPar(lst):
    s = 0
    for c in lst:
        if c % 2 == 0:
            s += c
    print(f'Somando os valores pares de {lst}, temos {s}')


num = []
sorteia(num)
somaPar(num)
