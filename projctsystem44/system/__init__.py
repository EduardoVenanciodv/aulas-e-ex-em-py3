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
    print(f'{linha()}\n{cor(dado, 'verde'):^50}\n{linha()}')


def cor(txt, tonalidade):
    if tonalidade == 'azul':
        return f'\033[34m{txt}\033[m'
    elif tonalidade == 'amarelo':
        return f'\033[33m{txt}\033[m'
    elif tonalidade == 'vermelho':
        return f'\033[31m{txt}\033[m'
    elif tonalidade == 'roxo':
        return f'\033[35m{txt}\033[m'
    elif tonalidade == 'verde':
        return f'\033[32m{txt}\033[m'


def leiainteiro(msg):
    try:
        resposta = int(input(cor(msg, 'amarelo')))
        if 1 <= resposta <= 3:
            return resposta
        else:
            print(f'{cor("Erro: Digite uma opção valida!", "vermelho")}')
    except (TypeError, ValueError):
        print(f'{cor("Erro: Digite um número inteiro valido!", 'vermelho')}')
    except KeyboardInterrupt:
        print(f'{cor("\nErro: O usuário decidiu não digitar nenhuma opção!", 'vermelho')}')

