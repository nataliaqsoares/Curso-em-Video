""" Desafio 069
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram
cadastrados. C) quantas mulheres tem menos de 20 anos. Caso erre, o programa deve solicitar a informação novamente """

mais_18 = homens = mulher_menos_20 = 0

while True:
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe o seu sexo: [M/F] ')).strip().lower()[0]
    while sexo != 'm' and sexo != 'f':
        sexo = str(input('Valor informado não aceito pelo sistema. Informe seu sexo novamente: [M/F] '))

    if idade > 18:
        mais_18 += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulher_menos_20 += 1

    continua = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while continua != 's' and continua != 'n':
        continua = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if continua == 'n':
        break

print(f'{mais_18} pessoas cadastradas tem mais de 18 anos\n{homens} homemens foram cadastrados\n{mulher_menos_20}'
      f' mulheres tem menos de 20 anos')
