""" Desafio 013
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento """

salario = float(input('Informe o seu salário: '))
aumento = salario * 0.15
novosalario = salario + aumento
print('O seu aumento foi de {:.2f}, com o valor final do seu salário ficando em {:.2f}'.format(aumento, novosalario))
