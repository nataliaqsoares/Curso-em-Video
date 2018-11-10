""" Desafio 072
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa
deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. """

num_ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatroze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Informe um número entre 0 e 20: '))
    while 0 > num or num > 20:
        num = int(input('Tente novamente. Informe um número entre 0 e 20:'))
    print(f'Você informou o número {num} que escrito por extenso é {num_ext[num]}')
    continuar = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Tente novamente. Deseja continuar? [S/N]')).strip().lower()[0]
    if continuar == 'n':
        break
print('Programa finalizado')
