"""Desafio 085
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""

num = [[], []]

for c in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)

num[0].sort()
num[1].sort()

print(f'Os valores pares digitador foram: {num[0]}\nOs valores ímpares digitados foram: {num[1]}')
