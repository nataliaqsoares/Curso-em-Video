""" Desafio 090
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
conteúdo da estrutura na tela. Obs.: se a média for 7 ou mais, está aprovado, se for < 7, recuperação, se for < 5 está
reprovado """

boletim = dict()

boletim['Aluno'] = str(input('Nome: '))
boletim['Media'] = float(input(f'Média de {boletim["Aluno"]}: '))

if boletim['Media'] >= 7:
    boletim['Situacao'] = 'Aprovado'
elif 5 <= boletim['Media'] < 7:
    boletim['Situacao'] = 'Recuperação'
elif boletim['Media'] < 5:
    boletim['Situacao'] = 'Reprovado'

for k, v in boletim.items():
    print(f'{k} = {v}')
