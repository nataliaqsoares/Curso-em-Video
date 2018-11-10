""" Desafio 023
Faça um programa que leia um número de 0 a 9999 e mostre na tela um dos dígitos separados.
Ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1 """

# Solução 1: com está solução só é possível obter o resulatdo esperado quando se coloca as quatro unidades
num = input('Digite um número entre 0 e 9999: ')
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(num[3], num[2], num[1], num[0]))

# Solução 2: com a lógica matematica é possível obter o resultado desejado independente de quantas unidades sejam usadas
n = int(input('Digite um número entre 0 e 9999: '))
u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('O número {} tem: \nUnidade(s): {} \nDezena(s): {} \nCentena(s): {} \nMilhar(es): {}'.format(n, u, d, c, m))
