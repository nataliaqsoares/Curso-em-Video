""" Desafio 031
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por
Km para viagens de até 200Km e R$ 0,45 para viagens mais longas. """

dist = int(input('Qual a distância da sua viagem? '))

if dist <= 200:
    passagem = dist * 0.5
else:
    passagem = dist * 0.45

print('A passagem para uma viagem de {}Km custa R$ {:.2f}'.format(dist, passagem))
