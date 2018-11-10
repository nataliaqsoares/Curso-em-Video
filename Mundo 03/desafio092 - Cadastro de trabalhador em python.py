""" Desafio 092
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario se
por acaso a CTPS for diferente de zero, o dicionario receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar. Obs.: Considerar que a pessoa se aposenta depois
de 35 anos de contribuição """

from datetime import date

ano_atual = date.today().year

prev = dict()
prev['Nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
prev['Idade'] = ano_atual - ano
prev['CTPS'] = int(input('Carteira de Trabalho (0 caso não tenha): '))

if prev['CTPS'] != 0:
    prev['Contratacao'] = int(input('Ano de contratação: '))
    prev['Salario'] = float(input('Salário: R$ '))
    prev['Aposentadoria'] = ((prev['Contratacao'] + 35) - ano)

print('=' * 20)
for k, v in prev.items():
    print(f'{k} = {v}')
