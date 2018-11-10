""" Desafio 024
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome Santo """

cidade = str(input('Informe o nome da sua cidade: ')).lower()
cidade = cidade.split()
print('santo' in cidade[0])
