""" Desafio 106
Faça um mini-sistema que uyilize o Interective Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Obs: use cores. """


def pyhelp():
    while True:
        from time import sleep
        print('Sistema de Ajuda PyHelp')
        msg = str(input('Função ou Biblioteca > ')).lower().strip()
        if msg == 'fim':
            print('Até logo!')
            break
        print(f'Acessando o manual do comando "{msg}"')
        sleep(0.5)
        help(msg)


# Programa Principal
pyhelp()
