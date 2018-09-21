""" Desafio 037
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1: para binário; 2: para octal; 3: para hexadecimal; """

num = int(input('Informe o número que deseja converter: '))
base = int(input('Informe para qual base deseja converter:\n[ 1 ] Binário\n[ 2 ] Octal\n[ 3 ] Hexadecimal\n'))

if base == 1:
    print(bin(num)[2:])
elif base == 2:
    print(oct(num)[2:])
elif base == 3:
    print(hex(num)[2:])
else:
    print('Base não reconhecida pelo sistema. Tente novamente.')
