""" Desafio 043
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
tabela abaixo: - Abaixo de 18.5: abaixo do peso; - Entre 18.5 e 25: peso ideal; - 25 até 30: sobrepeso; - 30 até 40:
obesidade; - Acima de 40: obesidade mórbida; """

peso = float(input('Informe o seu peso (Kg): '))
altura = float(input('Infome a sua altura (m): '))

imc = peso / (altura * altura)

if imc <= 18.5:
    print('Com o IMC de {:.1f} você está abaixo do peso ideal'.format(imc))
elif imc <= 25:
    print('Com o IMC de {:.1f} você está com o peso ideal'.format(imc))
elif imc <= 30:
    print('Com o IMC de {:.1f} você está com sobrepeso'.format(imc))
elif imc <= 40:
    print('Com IMC de {:.1f} você está com obesidade'.format(imc))
elif imc > 40:
    print('Com IMC de {:.1f} você está com obesidade mórbida'.format(imc))
