""" Desafio 026
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'
- Em que posição ela aparece pela primeira vez
- Em que posição ela aparece pela ultima vez """

frase = str(input('Digite uma frase: ')).lower().strip()
letras = frase.count('a')
primeiro = frase.find('a')
ultimo = frase.rfind('a')
print('A letra A aparece {} vezes na frase. \nA primeira letra A apareceu na posição {}. \nA útima letra A apareceu na'
      'posição {}.'.format(letras, primeiro + 1, ultimo + 1))

