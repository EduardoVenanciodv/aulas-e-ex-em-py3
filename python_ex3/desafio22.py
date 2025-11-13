jogador = {}
gol = list()
jogador['Nome'] = str(input('Digite o nome do jogador: '))
jogos = int(input(f'Digite quantos jogos o {jogador['Nome']} jogou:'))
for c in range(0, jogos):
    gol.append(int(input(f'Quantos gols na partida {c}:')))
jogador['Gols'] = gol[:]
jogador['Total'] = sum(gol)
print('=-'*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-'*20)
print(f'O jogador {jogador["Nome"]} jogou {jogos} partidas. ')
for n, g in enumerate(jogador['Gols']):
    print(f'{"=>":>6}Na partida {n}, fez {g} gols.')
print(f'Foi uma total de {jogador["Total"]} gols.')
