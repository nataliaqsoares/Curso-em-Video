""" Desafio 105
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as
seguintes informações: - Quantidade de notas;- A maior nota;- A menor nota;- A média da turma;- A situação (opcional)
Adicione também as docstrings da função. Obs.: Situação => 7 boa, =< 7 razoavel, =< 5 ruim"""


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionario com várias informações sobre a situação da turma
    """
    boletim = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': sum(n)/len(n)}
    if sit:
        if boletim['media'] <= 5:
            boletim['situacao'] = 'Ruim'
        elif boletim['media'] < 7:
            boletim['situacao'] = 'Razoável'
        elif boletim['media'] >= 7:
            boletim['situacao'] = 'Boa'
    return boletim


# Programa Principal
resp = notas(7.5, 7, 6.5, 7, 7, 7, sit=True)
print(resp)
help(notas)
