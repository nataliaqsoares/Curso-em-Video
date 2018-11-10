""" Desafio 034
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15% """

salario = float(input('Informe o seu salário: R$'))
if salario <= 1250:
    novo_salario = salario + (salario * 0.15)
else:
    novo_salario = salario + (salario * 0.10)
print('O seu salário atual é de R$ {:.2f} e com o aumento passará a ser de R$ {:.2f}'.format(salario, novo_salario))
