""" Desafio 077
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada
palavra, quais são as suas vogais """

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar',
            'Mercado', 'Programador', 'Futuro')

for palavra in palavras:
    print(f'Na palavra {palavra} temos as vogais: ', end='')
    for letra in palavra:
        if letra in 'AaEeIiOoUu':
            print(f'{letra}', end=' ')
    print('\n')
