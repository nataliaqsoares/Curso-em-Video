""" Desafio 093
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partidade. No final, tudo isso será guardado em
um dicionario, incluindo o total de gols feitos durante o campeonato. Obs.: a quantidade de gols deve ser guardado em
uma lista. """

jogador = dict()
gols = list()

jogador['Nome'] = str(input('Nome do jogador: '))
part = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, part):
    gols.append(int(input(f'Quantos gols na {c+1}º partida? ')))
jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)

print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'{k} = {v}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {part} partidas.')
for p, v in enumerate(jogador['Gols']):
    print(f'    => Na {p+1}º partida, fez {v} gols.')
print(f'No total foram feitos {jogador["Total"]} gols.')
