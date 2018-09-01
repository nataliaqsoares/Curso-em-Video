"""Desafio 020
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
que leia o nome dos quatro alunos e mostre a ordem sorteada"""

# Solução 1
import random

aluno1 = str(input('Informe o nome do primeiro aluno: '))
aluno2 = str(input('Informe o nome do segundo aluno: '))
aluno3 = str(input('Informe o nome do terceiro aluno: '))
aluno4 = str(input('Informe o nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem dos alunos escolhidos para apresentar o trabalho é: {}'.format(lista))

# Solução 2
from random import shuffle

aluno1 = input('Informe o nome do aluno: ')
aluno2 = input('Informe o nome de outro aluno: ')
aluno3 = input('Informe o nome de outro aluno: ')
aluno4 = input('Informe o nome de outro aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem dos alunos escolhidos para apresentar o trabalho é: {}'.format(lista))
