""" Desafio 046
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com
uma pausa de 1 segundo entre eles """

from time import sleep
from emoji import emojize

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emojize(""":sparkles: :sparkles: :sparkles: :sparkles: :sparkles: :sparkles: :sparkles: :sparkles: :sparkles:
:collision: :collision: :collision: :collision: :collision: :collision: :collision: :collision: :collision:
:anger: :anger: :anger: :anger: :anger: :anger: :anger: :anger: :anger:
:boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom: :boom:""", use_aliases=True))
