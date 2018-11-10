""" Desafio 038
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: - O primeiro valor é
maior; - O segundo valor é maior; - Não existe valor maior, os dois são iguais """

n1 = int(input('Informe um número: '))
n2 = int(input('Informe mais um número: '))

if n1 > n2:
    print('O primeiro valor é o maior')
elif n2 > n1:
    print('O segundo valor é o maior.')
else:
    print('Não há valor maior, os dois são iguais.')
