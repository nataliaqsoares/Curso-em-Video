""" Desafio 056
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: - a média de idade do
grupo; - qual é o nome do homem mais velho; - quantas mulheres têm menos de 20 anos """

soma_idade = 0
maior_idade = 0
cont = 0
nome_mais_velho = ''

for c in range(0, 4):
    nome = str(input('Informe o seu nome: ')).capitalize()
    idade = int(input('Informe a sua idade: '))
    sexo = str(input('Informe o seu sexo: [M/F]')).upper()
    soma_idade += idade
    
    if idade > maior_idade and sexo == 'M':
        maior_idade = idade
        nome_mais_velho = nome
    if idade < 20 and sexo == 'F':
        cont += 1

media = soma_idade / 4
print('A média de idade do grupo é de {:.1f} anos\nO nome do homem mais velho do grupo é {}\n{} mulher(es) do grupo tem'
      ' menos de 20 anos'.format(media, nome_mais_velho, cont))
