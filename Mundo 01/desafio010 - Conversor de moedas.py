""" Desafio 010
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
Considere US$ 1,00 = R$ 3,27 """

reais = float(input('Informe quantos reais tem na carteira: '))
dolares = reais / 3.27
print('Com {} reais você pode comprar {:.2f} dolares.'.format(reais, dolares))
