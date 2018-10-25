""" Desafio 087
Aprimore o desafio anterior, mostrando no final: a) a soma de todos os valores pares digitados b) a soma dos valores da
terceira coluna c) o maior valor da segunda linha. """

matriz = [[], [], []]
somapar = somacol = c = cont = 0

while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        somapar += n
    matriz[c].append(n)
    cont += 1
    if cont % 3 == 0:
        c += 1
        somacol += n
    if cont == 9:
        break
print('=' * 40)
for conj in matriz:
    for n in conj:
        print(f'[{n:^5}]', end=' ')
    print()
print('=' * 40)
print(f'A soma dos números pares é igual a {somapar}.\nA soma dos números da terceira coluna é igual a {somacol}.\n'
      f'O maior valor da segunda linha é {max(matriz[1])}.')

