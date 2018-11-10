""" Desafio 029
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
foi multado. A multa vai custar R$ 7,00 por km acima do limite. """

carro = float(input('Informe a velocidade do carro: '))
if carro > 80:
    multa = (carro - 80) * 7
    print('Você foi multado pois ultapassou o limite de velocidade de 80km/h. A multa foi de R$ {:.2f}'.format(multa))
print('Dirija com segurança!')
