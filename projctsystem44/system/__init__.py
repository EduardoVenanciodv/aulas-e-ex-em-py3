def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(cor(c, 'amarelo'), '-', cor(item, 'azul'))
        c += 1
    print(linha())
    opc = leiainteiro('Sua opção: ')
    return opc


def linha(linhas=42):
    return f'-'*linhas


def cabeçalho(dado):
    print(f'{linha()}\n{dado:^42}\n{linha()}')


def cor(txt, tonalidade):
    if tonalidade == 'azul':
        return f'\033[34m{txt}\033[m'
    elif tonalidade == 'amarelo':
        return f'\033[33m{txt}\033[m'
    elif tonalidade == 'vermelho':
        return f'\033[31m{txt}\033[m'


def leiainteiro(msg):
    resposta = int(input(cor(msg, 'amarelo')))
    try:
        if resposta == 1 or resposta == 2 or resposta == 3:
            return resposta
    except (TypeError, ValueError):
        print(f'{cor("Erro", 'vermelho')}')



