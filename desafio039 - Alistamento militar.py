""" Desafio 039
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar 'Faltam x anos para você se alistar';
- Se é a hora de se alistar 'Se aliste agora';
- Se já passou do tempo do alistamento 'Já passaram x anos do seu alistamento'.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo"""

from datetime import date

nasc = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - nasc

if idade < 18:
    print('Você tem {} anos e falta(m) {} ano(s) para você se alistar.'.format(idade, 18 - idade))
elif idade == 18:
    print('Você tem {} anos e precisa se alistar este ano.'.format(idade))
else:
    print('Você tem {} anos e deveria ter se alistado há {} anos atrás.'.format(idade, idade - 18))
