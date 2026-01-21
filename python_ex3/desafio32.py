
def ficha(nome = '<desconhecido>', gol = 0):
    """
    :param nome: Nome do jogador. Se o usuário não adicionar um nome, automaticamente irar ficar como deconhecido.
    :param gol: Gols do jogador. Se o usuário não adicionar valor, automaticamente irar ficar com 0 gols.
    :return: sem retorno
    """
    print(f'O jogador {nome}, tem {gol} gol(s) no campeonato.')


print('__'*10)
n = str(input('Nome do jogador:'))
g = str(input('Número de gols:'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
