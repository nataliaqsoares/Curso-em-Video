""" Desafio 065
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores """

continuar = 's'
maior = menor = soma = cont = 0

while continuar != 'n':
    num = int(input('Informe um número: '))
    if cont == 0:
        maior = menor = num
    soma += num
    cont += 1
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]

print('A média dos {} números digitados é {}\nO maior valor foi {} e o menor foi {}'
      .format(cont, (soma / cont), maior, menor))
