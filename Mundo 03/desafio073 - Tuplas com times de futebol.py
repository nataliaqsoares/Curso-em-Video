""" Desafio 073
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre: a) apenas os 5 primeiros colocados; b) os ultimos 4 colocados da tabela; c) uma lista com os
times em ordem alfabética; d) em que posição na tabela está o time da chapecoense """

times = ('Palmeiras', 'Internacional', 'São Paulo', 'Grêmio', 'Flamengo', 'Atlético Mineiro', 'Cruzeiro', 'Santos',
         'Corinthians', 'Fluminense', 'Atlético-PR', 'Botafogo', 'América-MG', 'Bahia', 'Ceará', 'Vasco da Gama',
         'Vitória', 'Chapecoense', 'Sport Recife', 'Paraná')

print('-' * 50)
print(f'Os cinco primeiros colocados da tabela são: {times[:5]}')
print('-' * 50)
print(f'Os quatro últimos colocados da tabela são: {times[-4:]}')
print('-' * 50)
print(f'Os times em ordem alfabetica são: {sorted(times)}')
print('-' * 50)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}º colocação')
