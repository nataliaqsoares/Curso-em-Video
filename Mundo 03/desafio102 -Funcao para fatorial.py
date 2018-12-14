""" Desafio 102
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de
cálculo do fatorial. Obs.: fazer uma docstring"""


def fatorial(n, show=False):
    """
    -> Calcula o Fatorail de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    print('-' * 30)
    for c in range(n, 0, -1):
        f *= c
        if show:
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
    return f


# Programa Principal
print(fatorial(5, True))
help(fatorial)
