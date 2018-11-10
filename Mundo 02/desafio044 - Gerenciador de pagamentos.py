""" Desafio 044
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento: - à vista dinheiro/cheque: 10% de desconto; - à vista no cartão: 5% de desconto; - em até 2x no cartão: preço
normal; - 3x ou mais no cartão: 20% de juros; """

produto = float(input('Qual o preço do produto? R$'))
pag = int(input('Como deseja pagar?\n[ 1 ] à vista no dinheiro ou cheque\n[ 2 ] à vista no cartão\n[ 3 ] 2x no cartão'
                '\n[ 4 ] 3x ou mais no cartão\n:'))

if pag == 1:
    novo_preco = produto - (produto * 0.1)
elif pag == 2:
    novo_preco = produto - (produto * 0.05)
elif pag == 3:
    novo_preco = produto
elif pag == 4:
    novo_preco = produto + (produto * 0.2)
    parc = int(input('Qauntas parcelas? '))
    print('Sua compra será parcelada em {} de {:.2f} com juros'.format(parc, novo_preco / parc))
else:
    novo_preco = produto
    print('Opção invalida. Tente novamente')
print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(produto, novo_preco))

