""" Desafio 076
Crie um programa que tenha uma tupla única com nomes de produtos e seus prestectivos preços, na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular """

produtos = ('Papel sulfite 500 folhas', 23.9, 'Caneta Esferográfica', 1.4, 'Caderno universitario 50 folhas', 21.8,
            'Cola branca 110g', 5.5, 'Lápis de cor 24 cores', 21.2, 'Caderno Universitário 200 folha', 12.1,
            'Post-it 100 folhas', 20.5)

print('=' * 50)
print(f'{"Produtos da Papelaria":^50}')
print('=' * 50)

for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<40}', end=' ')
    else:
        print(f'R$ {produtos[item]:>5.2f}')
