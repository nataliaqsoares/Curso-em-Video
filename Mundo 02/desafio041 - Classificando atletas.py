""" Desafio 041
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua catego_
ria, de acordo com a idade: - até 9 anos: mirim; - até 14 anos: infantil; - até 19 anos: junior;  - até 25 anos: sênior;
- acima: master; """

from datetime import date

nasc = int(input('Informe seu ano de nasciemnto: '))
idade = date.today().year - nasc

if idade <= 9:
    print('Com {} ano(s) o atleta pertence a categoria mirim'.format(idade))
elif idade <= 14:
    print('Com {} anos o atleta pertence a categoria infantil'.format(idade))
elif idade <= 19:
    print('Com {} anos o atleta pertence a categoria junior'.format(idade))
elif idade <= 25:
    print('Com {} anos o atleta pertence a categoria sênior'.format(idade))
elif idade > 25:
    print('Com {} anos o atleta pertence a categoria master'.format(idade))
