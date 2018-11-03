""" Desafio 097
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável. Obs.: Ajustar os traços ao tamanho da palavra"""


def escreva(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))


escreva('Aprenda Python')
escreva('Olá, Mundo!')
escreva('Natália Quintanilha')
