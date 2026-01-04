
def ficha(nome, gol):
    """
    :param nome: Nome do jogador. Se o usuário não adicionar um nome, automaticamente irar ficar como deconhecido.
    :param gol: Gols do jogador. Se o usuário não adicionar valor, automaticamente irar ficar com 0 gols.
    :return: sem retorno
    """
    if nome == '':
        nome = '<desconhecido>'
    if gol == '':
        gol = 0
    print(f'O jogador {nome}, tem {gol} gol(s) no campeonato.')


print('__'*10)
ficha(nome=str(input('Nome do jogador:')), gol=str(input('Número de gols:')))
