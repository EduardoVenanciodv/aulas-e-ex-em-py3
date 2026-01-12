
def ajuda():
    print('\033[35;40m~~'*16)
    print(f'{"Sistema de ajuda pyHelp":^32}')
    print('~~'*16)
    r = (input('\033[mFunção da biblioteca >').lower())
    if r == 'fim':
        print('\033[30;45m~~' * 16)
        print(f'{f"Fim.":^30}')
        print('~~' * 16)
        quit()
    else:
        print('\033[31;42m~~' * 16)
        print(f'{f"Acessando o manual de {r}.":^30}')
        print('~~' * 16)
        print('\033[m', end='')
        print(f'\033[7m')
        help(r)
        print(f'\033[m', end='')
        ajuda()


ajuda()
