"""Desafio 004
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
sobre ele"""

msg = input('Digite algo: ')
print('O valor {} e ele é do tipo primitivo desse valor é {}'.format(msg, type(msg)))
print('Esse valor é númerico? {}'.format(msg.isnumeric()))
print('Esse valor é alfabetico? {}'.format(msg.isalpha()))
print('Esse valor é alfanúmerico? {}'.format(msg.isalnum()))
print('Esse valor está todo em maiúsculo? {}'.format(msg.isupper()))
print('Esse valor está todo em minúsculo? {}'.format(msg.islower()))
print('Esse valor tem espaços? {}'.format(msg.isspace()))
print('Esse valor está capitalizado? {}'.format(msg.istitle()))
