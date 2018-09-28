""" Desafio 059
Crie um programa que leia dois valores e mostre um menu na tela: [1] somar; [2] multiplicar; [3] maior; [4] novos números
[5] sair do programa; Seu programa devera realizar a operação solicitada em cada caso. """

num1 = int(input('Informe um valor: '))
num2 = int(input('Informe mais um valor: '))
select = int(input('O que gostaria de fazer?\n[ 1 ] Soma\n[ 2 ] Multiplica\n[ 3 ] Qual o maior\n[ 4 ] Informar'
                   ' novamente os números\n[ 5 ] Sair\n'))

while select != 5:
    if select == 1:
        print('A soma de {} mais {} é igual a {}'.format(num1, num2, num1 + num2))
        print('=' * 40)
        select = int(input('O que gostaria de fazer?\n[ 1 ] Soma\n[ 2 ] Multiplica\n[ 3 ] Qual o maior\n[ 4 ] Informar'
                           ' novamente os números\n[ 5 ] Sair\n'))
    elif select == 2:
        print('A multiplicação de {} vezes {} é igual a {}'.format(num1, num2, num1 * num2))
        print('=' * 40)
        select = int(input('O que gostaria de fazer?\n[ 1 ] Soma\n[ 2 ] Multiplica\n[ 3 ] Qual o maior\n[ 4 ] Informar'
                           ' novamente os números\n[ 5 ] Sair\n'))
    elif select == 3:
        if num1 > num2:
            maior = num1
            print('Entre os números {} e {} o maior é {}'.format(num1, num2, maior))
        elif num2 > num1:
            maior = num2
            print('Entre os números {} e {} o maior é {}'.format(num1, num2, maior))
        else:
            print('Os dois números são iguais')
        print('=' * 40)
        select = int(input('O que gostaria de fazer?\n[ 1 ] Soma\n[ 2 ] Multiplica\n[ 3 ] Qual o maior\n[ 4 ] Informar'
                           ' novamente os números\n[ 5 ] Sair\n'))
    elif select == 4:
        print('=' * 40)
        num1 = int(input('Informe um valor: '))
        num2 = int(input('Informe mais um valor: '))
        select = int(input('O que gostaria de fazer?\n[ 1 ] Soma\n[ 2 ] Multiplica\n[ 3 ] Qual o maior\n[ 4 ] Informar'
                           ' novamente os números\n[ 5 ] Sair\n'))
    else:
        print('Opção invalida. Tente novamente')
        print('=' * 40)
        select = int(input('O que gostaria de fazer?\n[ 1 ] Soma\n[ 2 ] Multiplica\n[ 3 ] Qual o maior\n[ 4 ] Informar'
                           ' novamente os números\n[ 5 ] Sair\n'))
