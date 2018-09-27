""" Desafio 053
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex.: Apos a sopa / A sacada da casa / A torre da derrota / O lobo ama o bolo / Anotaram a data da maratona"""

frase = str(input('Informe uma frase: ')).lower().split()
frase = ''.join(frase)
cont_frase = len(frase)-1
cont = 0

for c in range(0, len(frase)):
    if frase[c] == frase[cont_frase]:
        cont += 1
    cont_frase -= 1
if len(frase) == cont:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')
