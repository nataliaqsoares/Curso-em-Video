""" Desafio 071
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Obs.: Considere que
o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1 """

saque = int(input('Informe o valor a ser sacado: R$ '))

if saque >= 50:
    notas = saque // 50
    saque -= notas * 50
    print(f'Foram sacadas {notas} notas de R$ 50')
if saque >= 20:
    notas = saque // 20
    saque -= notas * 20
    print(f'Foram sacadas {notas} notas de R$ 20')
if saque >= 10:
    notas = saque // 10
    saque -= notas * 10
    print(f'Foram sacadas {notas} notas de R$ 10')
if saque >= 1:
    notas = saque // 1
    saque -= notas * 1
    print(f'Foram sacadas {notas} notas de R$ 1')

print('Volte sempre!')

# Versão usando o while e listas (que ainda não foi mostrado)

saque = int(input('Informe o valor a ser sacado: R$ '))

cedula = [50, 20, 10, 1]
cont = 0

while True:
    if saque >= cedula[cont]:
        notas = saque // cedula[cont]
        saque -= notas * cedula[cont]
        print(f'Foram sacadas {notas} notas de R$ {cedula[cont]}')
    cont += 1
    if saque == 0:
        break

print('Volte sempre!')
