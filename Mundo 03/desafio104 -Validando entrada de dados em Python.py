""" Desafio 104
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python, só que
fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n') """


def leiaint(string):
    while True:
        num = input(string)
        if num.isnumeric():
            return num
        else:
            print('ERRO! Digite um número inteiro válido.')


# Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')