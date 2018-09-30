""" Desafio 063
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de
Fibonacci. Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 """

termo = int(input('Deseja ver quantos termos da sequência de fibonacci: '))
cont = n = 1
fibo = 0
print('0')
while termo != cont:
    n = n + fibo
    fibo = n - fibo
    cont += 1
    print('{}'.format(fibo))
