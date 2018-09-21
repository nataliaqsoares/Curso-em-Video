""" Desafio 036
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não
pode exceder 30% do salário ou então o empréstimo será negado. """

valor_casa = float(input('Qual valor da casa que deseja financiar? R$'))
salario = float(input('Qual seu salário mensal? R$'))
anos = int(input('Em quantos anos deseja pagar a casa? '))

prestacao = valor_casa / (anos * 12)

if prestacao >= (salario * 0.3):
    print('Infelizmente não foi possível financiar está casa no momento')
else:
    print('Seu financiamento foi aprovado! As prestações mensais para pagar a casa de {:.2f} em {} anos são de {:.2f}'
          .format(valor_casa, anos, prestacao))
