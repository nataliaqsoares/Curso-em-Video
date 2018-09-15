""" Desafio 032
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO """

ano = int(input('Informe o ano que deseja saber se é bissexto: '))
if ano % 4 == 0:
    if ano % 100 != 0:
        print('O ano {} é bissexto'.format(ano))
    else:
        print('O ano {} não é bissexto'.format(ano))
else:
    if ano % 400 == 0:
        print('O ano {} é bissexto'.format(ano))
    else:
        print('O ano {} não é bissexto'.format(ano))
