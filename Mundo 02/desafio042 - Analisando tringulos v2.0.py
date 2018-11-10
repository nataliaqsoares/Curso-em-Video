""" Desafio 042
Refaça o defsaio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais; - Isósceles: dois lados iguais; - Escaleno: todos os lados diferentes; """

reta1 = float(input('Informe o valor da primeira reta:'))
reta2 = float(input('Informe o valor da segunda reta:'))
reta3 = float(input('Informe o valor da terceira reta:'))

if (reta2 - reta3) < reta1 < reta2 + reta3 and (reta1 - reta3) < reta2 < reta1 + reta3 and (reta1 - reta2) < reta3 < \
        reta1 + reta2:
    if reta1 == reta2 == reta3:
        print('As retas podem formar um triângulo equilátero.')
    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
        print('As retas podem formar um triângulo isósceles')
    else:
        print('As retas podem formar um triângulo escaleno')
else:
    print('Essas retas não podem formam um triângulo')
