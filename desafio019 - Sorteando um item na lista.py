"""Desafio 019
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
deles e escrevendo o nome escolhido."""

# Solução 1

import random
aluno1 = str(input('Informe o nome do primero aluno: '))
aluno2 = str(input('Informe o nome do segundo aluno: '))
aluno3 = str(input('Informe o nome do terceiro aluno: '))
aluno4 = str(input('Informe o nome do quarto aluno: '))
escolhido = random.choice([aluno1, aluno2, aluno3, aluno4])
print('O aluno escolhido para apagar o quadro foi: {}'.format(escolhido))

# Solução 2

from random import choice
aluno1 = input('Informe o nome do aluno: ')
aluno2 = input('Informe o nome de outro aluno: ')
aluno3 = input('Informe o nome de outro aluno: ')
aluno4 = input('Informe o nome de outro aluno: ')
escolhido = choice([aluno1, aluno2, aluno3, aluno4])
print('O aluno escolhido para apagar o quadro foi: {}'.format(escolhido))
