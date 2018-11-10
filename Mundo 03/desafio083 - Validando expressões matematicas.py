""" Desafio 083
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
expressão passada está com os parênteses abertos e fechados na ordem correta """

cont = 0
exp = str(input('Digite a sua expressão:'))
for c in exp:
    if c == ')' or c == '(':
        cont += 1
if cont % 2 == 0:
    print('A sua expressão está certa')
else:
    print('A sua expressão está errada')
