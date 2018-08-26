""" Desafio002.1
Crie um programa que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data
formatada (mensagem de saida = Você nasceu no dia x de x de x. Correto?)"""

# Solução 1
nasc = input('Quando você nasceu? ')
print('Você nasceu em', nasc, 'Correto?')

# Solução 2
dia = input('Em qual dia você nasceu? ')
mes = input('Em qual mês você nasceu? ')
ano = input('Em qual ano você nasceu? ')
print('Você nasceu no dia', dia, 'de', mes, 'de', ano, 'Correto?')
