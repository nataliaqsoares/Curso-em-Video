""" Desafio 075
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: a) quantas vezes
apareceu o valor 9; b) em que posição foi digitado o primeiro valor 3; c) quais foram os números pares; """

n1 = int(input('Informe um número: '))
n2 = int(input('Informe mais um número: '))
n3 = int(input('Informe mais um número: '))
n4 = int(input('Informe o último número: '))

conjunto = (n1, n2, n3, n4)

print(f'Foram informados os números: {conjunto}')
print(f'O 9 apareceu {conjunto.count(9)} vezes')
if conjunto.count(3) == 0:
    print(f'O número 3 não foi informado')
else:
    print(f'O 3 apareceu na {conjunto.index(3) + 1}º posição')
print(f'Os números pares digitados foram: ', end='')

for num in conjunto:
    if num % 2 == 0:
        print(num, end=' ')
