""" Desafio 089
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
Obs.: usar 999 para interromper a mostragem de notas individuais de alunos """

from time import sleep

boletim = list()
alunos = list()
notas = list()
inter = media = nota = 0

while True:
    alunos.append(str(input('Nome: ')).capitalize())
    for c in range(0, 2):
        nota = float(input(f'Nota {c+1}: '))
        media += nota
        notas.append(nota)
    alunos.append(notas[:])
    notas.clear()
    media = media / 2
    alunos.append(media)
    media = 0
    boletim.append(alunos[:])
    alunos.clear()
    continuar = str(input('Deseja continuar? ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? ')).strip().lower()[0]
    if continuar == 'n':
        break

print('=' * 50)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for p, aluno in enumerate(boletim):
    print(f'{p:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
print('=' * 50)

while True:
    inter = int(input('Deseja mostrar as notas de qual aluno? (999 para interromper): '))
    if inter == 999:
        print('Finalizando o programa...')
        sleep(2)
        break
    print(f'As notas de {boletim[inter][0]} foram: {boletim[inter][1]}')
    print('=' * 50)
print('Volte sempre!!!')
