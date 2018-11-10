""" Desafio 061
Refaça o Defasio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progreção usando
a estrutura while """

inicio = int(input('Informe o primeiro termo da progressão aritmetica: '))
razao = int(input('Informe a razão da progressão: '))

pa = cont = 0

while cont < 9:
    if cont == 0:
        pa = inicio + razao
        cont += 1
        print('{}º termo: {}'.format(cont, inicio))
    else:
        pa += razao
        cont += 1
    print('{}º termo: {}'.format(cont + 1, pa))
