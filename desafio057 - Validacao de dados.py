""" Desaio 057
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado peça a digítação
novamente até ter um valor correto."""

sexo = str(input('Informe o seu sexo: [M/F]')).strip().lower()
while sexo != 'm' and sexo != 'f':
    sexo = str(input('Sexo informado não aceito pelo sistema. Informe seu sexo novamente: [M/F]')).strip().lower()
print('Sexo registrado com sucesso')
