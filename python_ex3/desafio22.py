jogador = {}
gol = list()
tot = 0
jogador['Nome'] = str(input('Digite o nome do jogador: '))
jogos = int(input(f'Digite quantos jogos o {jogador['Nome']} jogou:'))
for c in range(0, jogos):
    jogogol = int(input(f'Quantos gols na partida {c}:'))
    gol.append(jogogol)
    jogador['Gols'] = gol
    tot += jogogol
    jogador['Total'] = tot
print('=-'*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-'*20)
print(f'O jogador {jogador["Nome"]} jogou {jogos} partidas. ')
for n, g in enumerate(jogador['Gols']):
    print(f'{"=>":>6}Na partida {n}, fez {g} gols.')
