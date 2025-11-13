grupo = []
jogadores = {}
gol = []
while True:
    print('__'*30)
    jogadores.clear()
    jogadores['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantos jogos o {jogadores["nome"]} jogou?'))
    gol.clear()
    for c in range(0, jogos):
        gol.append(int(input(f'Quantos gols na partida {c + 1}?')))
    jogadores['gols'] = gol[:]
    jogadores['soma_gols'] = sum(gol)
    grupo.append(jogadores.copy())
    while True:
        continuar = str(input('Quer continuar (S/N)?')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if continuar == 'N':
        break
print('-=' * 30)
print(f'{"COND":<4} {"NOME":<8} {"GOLS":>10} {"TOTAL":>15}')
print('__'*20)
for c, b in enumerate(grupo):
    print(f'{c:>4} ', end='')
    for v in b.values():
        print(f'{str(v):<15}', end='')
    print()
print('=-'*20)
while True:
    dados = int(input('Mostra dados de qual jogador?'))
    if dados == 999:
        break
    elif dados >= len(grupo):
        print(f'Erro! Não existe jogador com o código {dados}! Tente novamente.')
    else:
        print(f'-- Levantamento do jogador {grupo[dados]["nome"]}')
        for n, v in enumerate(grupo[dados]["gols"]):
            print(f'{"No":>5} jogo {n + 1} fez {v} gols')
    print('=-'*20)
print(f'{"<---Volte Sempre--->":^35}')
