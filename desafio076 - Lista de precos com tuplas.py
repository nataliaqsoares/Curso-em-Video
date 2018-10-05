""" Desafio 076
Crie um programa que tenha uma tupla única com nomes de produtos e seus prestectivos preços, na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular. """

produtos = ('Papel sulfite 500 folhas', 23.9, 'Caneta Esferográfica', 1.4, 'Caderno universitario 50 folhas', 21.8,
            'Cola branca 110g', 5.5, 'Lápis de cor 24 cores', 21.2, 'Caderno Universitário 200 folha', 12.1,
            'Post-it 100 folhas', 20.5)
print('=' * 50)
print('Produtos da Papelaria')
print('=' * 50)
print(f'{produtos[0]:.<40} R$ {produtos[1]:.2f}\n'
      f'{produtos[2]:.<40} R$ {produtos[3]:.2f}\n'
      f'{produtos[4]:.<40} R$ {produtos[5]:.2f}\n'
      f'{produtos[6]:.<40} R$ {produtos[7]:.2f}\n'
      f'{produtos[8]:.<40} R$ {produtos[9]:.2f}\n'
      f'{produtos[10]:.<40} R$ {produtos[11]:.2f}\n'
      f'{produtos[12]:.<40} R$ {produtos[13]:.2f}')
