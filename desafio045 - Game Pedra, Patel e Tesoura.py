""" Desafio 045
Crie um programa que faça o computador jogar jokenpô com você """

from random import randint

print('Vamos jogar Jokenpô!!!')
pc = randint(1, 3)
jog = int(input('Escolha um:\n[ 1 ] Pedra\n[ 2 ] Tesoura\n[ 3 ] Papel\n:'))

if pc == 1 and jog == 1:
    print('Empatamos. Vamos jogar de novo?')
elif pc == 1 and jog == 2:
    print('Eu ganhei! Pedra ganha da tesoura. Vamos jogar de novo?')
elif pc == 1 and jog == 3:
    print('Eu perdi... Pedra perde para papel. Vamos jogar de novo?')
elif pc == 2 and jog == 1:
    print('Eu perdi... Tesoura perde para pedra. Vamos jogar de novo?')
elif pc == 2 and jog == 2:
    print('Empatamos. Vamos jogar de novo?')
elif pc == 2 and jog == 3:
    print('Eu ganhei! Tesoura ganha do papel. Vamos jogar de novo?')
elif pc == 3 and jog == 1:
    print('Eu ganhei! Papel ganha da pedra. Vamos jogar de novo?')
elif pc == 3 and jog == 2:
    print('Eu perdi... Papel perde para tesoura. Vamos jogar de novo?')
elif pc == 3 and jog == 3:
    print('Empatamos. Vamos jogar de novo?')
else:
    print('Jogada invalida. Tente novamente.')
