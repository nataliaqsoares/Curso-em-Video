"""Desafio 008
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros"""

m = float(input('Informe o valor em metros: '))
cm = m * 100
mm = m * 1000
print('O valor de {}m vale {}cm e {}mm.'.format(m, cm, mm))
