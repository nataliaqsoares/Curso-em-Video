""" Desafio 095
Aprimore o dasafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
aproveitamento de cada jogador. Obs.: Caso seja digitado um jogardor que não esta na lista, gerar um erro. Usar a flag
999 para fazer o programa parar """

time = list()
jogador = dict()
gols = list()

while True:
    print('-=' * 20)
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na {c+1}º partida? ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    gols.clear()
    time.append(jogador.copy())
    continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break

print('-=' * 30)
print(f'{"cod":<4}{"Nome":<15}{"Gols":<15}{"Total":<15}')
for p, jog in enumerate(time):
    print(f'{p:<4}', end='')
    for dado in jog.values():
        print(f'{str(dado):<15}', end='')
    print()

while True:
    inter = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if inter == 999:
        break
    if inter >= len(time):
        print('Este jogador não existe. Tente novamente')
    else:
        print('-=' * 30)
        print(f'Levantamento do jogador {time[inter]["Nome"]}')
        for pos, gol in enumerate(time[inter]['Gols']):
            print(f'No {pos+1}º jogo fez {gol} gols.')

print('Programa encerrado')
