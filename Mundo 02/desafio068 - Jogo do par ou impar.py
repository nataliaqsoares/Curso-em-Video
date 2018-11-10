""" Desafio 068
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo. """

from random import randint

print('Vamos jogar par ou ímpar! Qual você escolhe?')
cont = 0

while True:
    pc = randint(0, 10)
    jog = str(input('Par ou Ímpar: ')).lower().strip()[0]
    jog_num = int(input('Diga um número: '))
    soma = pc + jog_num

    if soma % 2 == 0 and jog == 'p':
        print(f'Você jogou {jog_num} e eu joguei {pc} que da {soma}. Você ganhou!')
        cont += 1
    elif soma % 2 == 0 and jog == 'i':
        print(f'Você jogou {jog_num} e eu joguei {pc} que da {soma}. Você perdeu!')
        break
    elif soma % 2 != 0 and jog == 'p':
        print(f'Você jogou {jog_num} e eu joguei {pc} que da {soma}. Você perdeu!')
        break
    elif soma % 2 != 0 and jog == 'i':
        print(f'Você jogou {jog_num} e eu joguei {pc} que da {soma}. Você ganhou!')
        cont += 1
print(f'No total você ganhou {cont} vez(es)')
