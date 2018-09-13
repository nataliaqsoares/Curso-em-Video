""" Desafio 022
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas;
- O nome com todas minúsculas;
- Quantas letras tem ao todosem considerar espaços
- Quantas letras tem o primeiro nome """

nome = str(input('Informe seu nome completo: '))
maiusculo = nome.upper()
minusculo = nome.lower()
nome = nome.split()
letras = len(''.join(nome))
print('Seu nome em maiúsculo é {}\nSeu nome em minúsculo é {} \nSeu nome tem ao todo {} letras \nSeu primeiro nome é {}'
      ' e ele tem {} letras'
      .format(maiusculo, minusculo, letras, nome[0], len(nome[0])))
