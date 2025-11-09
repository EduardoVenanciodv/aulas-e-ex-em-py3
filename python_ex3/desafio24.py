grupo = []
jogadores = {}
gol = []
cont = 0
while True:
    print('__'*30)
    jogadores['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantos jogos o {jogadores["nome"]} jogou?'))
    totgol = 0
    for c in range(0, jogos):
        gols = int(input(f'Quantos gols na partida {c}?'))
        gol.append(gols)
        totgol += gols
    jogadores['gols'] = gol[:]
    jogadores['soma_gols'] = totgol
    grupo.append(jogadores.copy())
    gol.clear()
    cont += 1
    print(grupo)
    continuar = str(input('Quer continuar (S/N)?')).upper().strip()[0]
    if continuar == 'N':
        print('-=' * 30)
        break
print(f'{"COND":<4} {"NOME":<8} {"GOLS":>8} {"TOTAL":>16}')
print('__'*20)
for c, b in enumerate(grupo):
    print(f'{c:<4} {b["nome"]:<12} {b["gols"]} {b["soma_gols"]:>8}')

while True:
    print('=-'*20)
    dados = int(input('Mostra dados de qual jogador?'))
    if dados == 999:
        break
    elif dados > cont - 1:
        print(f'Erro! Não existe jogador com o código {dados}! Tente novamente.')
    elif dados <= cont - 1:
        print(f'-- Levantamento do jogador {grupo[dados]["nome"]}')
        for n, v in enumerate(grupo[dados]["gols"]):
            print(f'{"No":>5} jogo {n} fez {v} gols')
print(f'{"<---Volte Sempre--->":^35}')
