""" Desafio 062
Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele
disser que quer mostrar 0 termos """

inicio = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razao: '))

termo = inicio
termos = cont = 0
mais = 10

while mais != 0:
    print('{}º termo: {}'.format(termos + 1, termo))
    termo += razao
    termos += 1
    cont += 1
    if cont == mais:
        print('-' * 32)
        mais = int(input('Deseja ver mais quantos termos? Coloque 0 caso não queira ver mais nenhum '))
        cont = 0

print('Programa finalizado')
