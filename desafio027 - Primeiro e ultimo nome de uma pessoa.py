""" Desafio 027
Faça um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex.: Ana Maria de Souza
primeiro = Ana
último = Souza """

nome = input('Informe seu nome completo: ')
nome = nome.split()
print('Seu primeiro nome é {} \nSeu último nome é {}'.format(nome[0], nome[len(nome) - 1]))
