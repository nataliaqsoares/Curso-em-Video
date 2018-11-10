""" Desafio 039.1
Faça um programa que leia o ano de nascimento e o sexo dos jovem e informe, de acordo com sua idade e sexo:
- Se for do sexo feminino, informar que não há necessidade de fazer o alistamento;
- Se for do sexo masculino, verificar a idade e informar:
- Se ele ainda vai se alistar ao serviço militar 'Faltam x anos para você se alistar';
- Se é a hora de se alistar 'Se aliste agora';
- Se já passou do tempo do alistamento 'Já passaram x anos do seu alistamento'.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo"""

from datetime import date

nasc = int(input('Informe o seu ano de nascimento: '))
sexo = str(input('Informe o seu sexo: [F/M]')).strip().upper()

idade = date.today().year - nasc

if sexo == 'F':
    print('Pela legislação você não é obrigada a fazer o alistamento.')
elif sexo == 'M':
    if idade < 18:
        print('Você tem {} anos e falta(m) {} ano(s) para seu alistamento.'.format(idade, 18 - idade))
    elif idade == 18:
        print('Você tem 18 anos e precisa se alistar este ano.')
    elif idade > 18:
        print('Você tem {} idade e deveria ter feito seu alistamento a {} anos.'.format(idade, idade - 18))
else:
    print('Sexo não reconhecido. Tente novamente.')
