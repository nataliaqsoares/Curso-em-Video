"""Desafio 005
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor"""

n = int(input('Digite um número: '))
print('O número {} tem como sucessor {} e antecessor {}.'.format(n, n+1, n-1))
