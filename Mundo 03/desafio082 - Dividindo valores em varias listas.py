""" Desafio 082
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
geradas """

valores = list()
par = list()
impar = list()

while True:
    valores.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break

for valor in valores:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

print(f'A lista completa tem os números: {valores}\nOs números pares são: {par}\nOs números ímpares são: {impar}')
