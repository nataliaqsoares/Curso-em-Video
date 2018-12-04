""" Desafio 101
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições. Obs.: Após os
65 anos o ovo é opcional"""


def voto(data):
    from datetime import date
    idade = date.today().year - data
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


nasc = int(input('Informe em que ano você nasceu: '))
print(voto(nasc))
