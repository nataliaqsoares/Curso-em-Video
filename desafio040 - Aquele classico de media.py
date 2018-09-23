""" Desafio 040
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
média atingida: -Média abaixo de 5.0: reprovado -Média entre 5.0 e 6.9: recuperação -Média 7.0 ou superior: aprovado"""

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('Você foi reprovado. Sua média foi de {}'.format(media))
elif media <= 6.9:
    print('Você está de recuperação. Sua média foi de {}'.format(media))
elif media >= 7.0:
    print('Você foi aprovado. Sua média foi de {}'.format(media))
