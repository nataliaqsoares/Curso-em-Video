"""Desafio 011
Faça um programa que leia a largura e a altura de uma parade em metros, calcule a sua área e quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²"""

altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))
area = altura * largura
tinta = area / 2
print('Para pintar uma parede de {}m² serão necessarios {:.1f} litros de tinta'.format(area, tinta))
