""" Desafio 027
Faça um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex.: Ana Maria de Souza
Primeiro = Ana
Último = Souza """

nome = str(input('Informe seu nome completo: ')).split()
print('Seu primeiro nome é {} \nSeu último nome é {}'.format(nome[0], nome[len(nome) - 1]))
