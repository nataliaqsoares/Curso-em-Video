""" Desafio 094
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionario e
todos os dicionarios em uma lista. No final, mostre: a) Quantas pessoas foram cadastradas b) a media de idade do grupo
c) uma lista com todas as mulheres d) uma lista com todas as pessoas com idade acima da media """

pessoa = dict()
grupo = list()
media = 0

while True:
    pessoa['Nome'] = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] '))
    while sexo not in 'MmFf':
        sexo = str(input('Erro! Por favor digite apenas M ou F.\nSexo: [M/F] '))
    pessoa['Sexo'] = sexo
    pessoa['Idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    media += pessoa['Idade']
    continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break

print('-=' * 30)
print(f'O grupo tem {len(grupo)} pessoas')
print(f'A média de idade é de {media/len(grupo)} anos.')
print(f'As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['Sexo'] in 'Ff':
        print(p['Nome'], end=' ')

print(f'\nA lista de pessoas acima da média de idade são: ')
for pes in grupo:
    if pes['Idade'] > media/len(grupo):
        for k, v in pes.items():
            print(f'{k} = {v}', end='; ')
        print()
