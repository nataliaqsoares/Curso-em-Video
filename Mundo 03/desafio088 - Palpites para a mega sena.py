""" Desafio 088
Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta """

# Solução com lista simples
from random import randint
from time import sleep

mega = list()
jogos = int(input('Quantos jogos você quer que eu sorteie? '))

for cont in range(0, jogos):
    for c in range(0, 6):
        n = randint(1, 60)
        while n in mega:
            n = randint(1, 60)
        mega.append(n)
    mega.sort()
    print(f'Jogo {cont+1}: {mega}')
    sleep(2)
    mega.clear()

# Solução com lista composta
from random import randint
from time import sleep

mega = list()
jogo = list()
jogos = int(input('Quantos jogos você quer sortear? '))

for cont in range(0, jogos):
    for c in range(0, 6):
        n = randint(1, 60)
        while n in jogo:
            n = randint(1, 60)
        jogo.append(n)
    mega.append(jogo[:])
    jogo.clear()

for p, jog in enumerate(mega):
    print(f'Jogo {p+1}: {jog}')
    sleep(2)
