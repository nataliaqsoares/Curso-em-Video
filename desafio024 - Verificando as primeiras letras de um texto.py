""" Desafio 024
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo' """

cidade = input('Informe o nome da sua cidade: ')
cidade = cidade.split()
print('Santo' in cidade[0])
