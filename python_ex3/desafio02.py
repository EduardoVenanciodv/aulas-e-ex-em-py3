serieA = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Mirassol', 'Botafogo', 'Bahia', 'São Paulo',
          'Fluminense', 'Bragantino-RB', 'Corinthians', 'Grêmio', 'Ceará', 'Vasco', 'Internacional',
          'Santos', 'Atlético-MG', 'Vitória', 'Juventude', 'Fortaleza', 'Sport')
serieB = ('Criciúma', 'Goiás', 'Coritiba', 'Novorizontino', 'Athletico-PR', 'Cuiabá', 'Chapecoense',
          'Atlético-GO', 'CRB', 'Avaí', 'Operário-PR', 'Remo', 'Vila Nova', 'Ferroviária-SP',
          'Athletic Club (MG)', 'América-MG', 'Volta Redonda', 'Botafogo-SP', 'Amazonas', 'Paysandu', )
print('-='*15)
print(f'Classificação do Brasileirão:{serieA}')
print('-='*15)
print(f'Os 5 primeros colocados são : {serieA[0:5]}')
print('-='*15)
print(f'Os 4 últimos times da tabela são : {serieA[-4:]}')
print('-='*15)
print(f'Classificação do Brasileirão em ordem alfabética : {sorted(serieA)}')
print('-='*15)
a = serieB.index('Chapecoense') + 1
print(f'Infelizmente a Chapecoense está atualmente na serie B, na {a}^ colocação.')
print('-='*15)

saida = 'S'
while saida == 'S':
    iniciar = str(input('O time que você quer saber a colocação está na serie A ou B?')).upper().strip()[0]
    if iniciar == 'A':
        name = str(input('Digite o nome do time:'))
        classific = serieA.index(name)+1
        print(f'O {name} está na {classific}^ colocação da serie A.')
        saida = str(input('Você quer ver outro time (S/N)?')).upper().strip()[0]
    elif iniciar == 'B':
        name = str(input('Digite o nome do time:'))
        classific = serieB.index(name)+1
        print(f'O {name} está na {classific}^ colocação da serie B.')
        saida = str(input('Você quer ver outro time (S/N)?')).upper().strip()[0]
    else:
        print('Erro')
        print('Tente novamente.', end=' ')
