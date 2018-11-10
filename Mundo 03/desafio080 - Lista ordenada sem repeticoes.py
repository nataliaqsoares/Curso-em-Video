""" Desafio 080
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela """

# Respostas do Guanabara

lista = []  # Cria uma lista vazia

for c in range(0, 5):
    n = int(input('Digite um valor: '))  # Le o valor sem adicionar a lista
    # Verifica se é o primeiro elemento a ser adicionado a lista ou se é maior que o elemento da lista
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):  # Varre a lista até o momento
            if n <= lista[pos]:  # Verifica se n é menor ou igual a um valor na lista em determinada posição
                lista.insert(pos, n)  # Caso seja menor, o n será inserido na posição desse valor
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print(f'Os valores digitados em ordem foram {lista}')
