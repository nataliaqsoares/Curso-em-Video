""" Desafio 078
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista."""

valores = list()

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor: ')))

print(f'Os 5 números digitados foram: {valores}')

print(f'O menor número digitado foi {min(valores)} e está nas posições ', end='')
for c, v in enumerate(valores):
    if min(valores) == v:
        print(valores.index(min(valores), c), end='... ')

print(f'\nO maior número digitado foi {max(valores)} e está nas posições ', end='')
for c, v in enumerate(valores):
    if max(valores) == v:
        print(valores.index(max(valores), c), end='... ')
