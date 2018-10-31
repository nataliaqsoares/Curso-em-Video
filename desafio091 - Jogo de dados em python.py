""" Desafio 091
Crie um programa onde 4 jogadores joguem um dado (1 a 6) e tenham resultados aleatórios. Guarde esses resultados em um
dicionario. No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior número no dado.
Obs.: haverá pequnas pausas antes do proximo resultado ser mostrado. Mostrar os valores sorteados e depois o ranking"""

from random import randint
from operator import itemgetter
from time import sleep

jogos = {}

for c in range(0, 4):
    jogos[f'Jogador {c+1}'] = randint(1, 6)

print('Os números sorteados foram:')
for k, v in jogos.items():
    print(f'    {k} com {v}')
    sleep(1)

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores: ')
for v, p in enumerate(ranking):
    print(f'    {v+1}º: {p[0]} com {p[1]}')
    sleep(1)
