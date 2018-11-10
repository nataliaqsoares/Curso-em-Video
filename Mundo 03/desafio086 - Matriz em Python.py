""" Desafio 086
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a
matriz na tela, com a formatação correta """

matriz = [[], [], []]

c = cont = 0

while True:
    n = int(input('Digite um número: '))
    matriz[c].append(n)
    cont += 1
    if cont % 3 == 0:
        c += 1
    if cont == 9:
        break

for conj in matriz:
    for n in conj:
        print(f'[{n:^5}]', end=' ')
    print()
