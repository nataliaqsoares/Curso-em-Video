"""Desafio 010
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares, euros, libras, ienes,
pesos argentinos e iuanes ela pode comprar. Considere US$ 1,00 = R$ 4,1193; EUR$ 1,00 = R$ 4,7969; GBP 1,00 = R$ 5,3519;
JPY$ 1,00 = R$ 0,0372; ARS$ 1,00 = R$ 0,1075; CNY 1,00 = R$ 0,6029 """

real = float(input('Quantos reais tem na carteira? R$'))
dolar = real / 4.1193
euro = real / 4.7969
libra = real / 5.3519
iene = real / 0.0372
peso = real / 0.1075
iuanes = real / 0.6029
print('Com {:.2f} reais é possivel comprar: \n{:.2f} dolares \n{:.2f} euros \n{:.2f} libras esterlinas \n{:.2f} ienes'
      '\n{:.2f} pesos argentinos \n{:.2f} iuanes'.format(real, dolar, euro, libra, iene, peso, iuanes))
