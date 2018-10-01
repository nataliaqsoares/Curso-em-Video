""" Desafio 070
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre: A) Qual é o total gasto na compra. B) Quantos produtos custam mais de R$ 1000. C) Qual é o nome do
produto mais barato. """

gasto = caro = barato = 0

while True:
    nome_produto = str(input('Informe o nome do produto: ')).strip()
    preco_produto = float(input('Informe o preço do produto: R$ '))

    gasto += preco_produto
    if preco_produto > 1000:
        caro += 1
    if barato == 0:
        barato = preco_produto
        produto_barato = nome_produto
    if preco_produto < barato:
        barato = preco_produto
        produto_barato = nome_produto

    continua = str(input('Deseja continuar: [S/N] ')).strip().lower()[0]
    if continua == 'n':
        break
print(f'O total gasto nessa compra foi de R$ {gasto:.2f}\n{caro} custam mais de R$ 1000.00\nO produto mais barato foi '
      f'{produto_barato} que custou R$ {barato:.2f}')
