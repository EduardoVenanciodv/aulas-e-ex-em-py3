def moeda(p):
    return f'R${p:.2f}'.replace('.', ',')


def metade(p, sit=False):
    if sit:
        p = p * 0.5
        return moeda(p)
    return p * 0.5


def dobro(p, sit=False):
    if sit:
        p = p * 2
        return moeda(p)
    return p * 2


def aumento(p, a, sit=False):
    if sit:
        p = (a / 100) * p + p
        return moeda(p)
    return (a / 100) * p + p


def diminuir(p, d, sit=False):
    if sit:
        p = p - (d / 100) * p
        return moeda(p)
    return p - (d / 100) * p


def resumo(p, a, d):
    print('--' * 18)
    print(f'{"Resumo Do Valor":^36}')
    print('--' * 18)
    matriz = [['Preço analisado:', 'Dobro do preço:', 'Metade do preço:', f'{a}% de aumento:', f'{d}% de redução:'],
              [f'{moeda(p)}', f'{dobro(p, True)}', f'{metade(p, True)}',
               f'{aumento(p, a, True)}', f'{diminuir(p, d, True)}']]

    for c in range(len(matriz[0])):
        print(f'{matriz[0][c]:<25}', end=' ')
        print(f'{matriz[1][c]}')
    print('--' * 18)

