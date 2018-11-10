""" Desafio 048
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
intervalo de 1 até 500 """

s = 0
n = 0

for c in range(1, 501):
    if c % 3 == 0:
        if c % 2 != 0:
            s += c
            n += 1

print('A soma dos {} números ímpares múltiplos de 3 entre 1 e 500 é de {}'.format(n, s))
