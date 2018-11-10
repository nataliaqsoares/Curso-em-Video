""" Desafio 058
Melhore o jogo do Desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer """

from random import randint

pc = randint(0, 10)

print('Estou pensando em um número entre 0 e 10... Tente adivinhar!')
jog = int(input('Em qual número pensei? '))

cont = 1

while pc != jog:
    print('Você errou...')
    jog = int(input('Tente novamente! Em qual número pensei? '))
    cont += 1

print('Parabens, você acertou, mas precisou de {} tentativas para acertar!'.format(cont, pc))
