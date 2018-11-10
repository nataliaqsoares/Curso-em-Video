""" Desafio 081
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: a) quantos números foram
digitados. b) a lista de valores ordenada de forma decrescente; c) se o valor 5 foi digitado e está ou não na lista """

valores = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? ')).strip().lower()[0]
    if continuar == 'n':
        break

valores.sort(reverse=True)
print(f'Foram digitados ao todo {len(valores)} números.\nO números em ordem decrescente ficam: {valores}')
if 5 in valores:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
