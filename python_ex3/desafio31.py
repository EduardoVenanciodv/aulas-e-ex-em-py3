
def fatorial(n=1, show=False):
    """
    --> Calcula o valor fatorial de um número
    :param n: O valor a ser calculado
    :param show: (opcinal) Mostrar ou não a conta, por padrão 'False'
    :return: O valor do fatorial de um número n

    """
    f = 1
    print('__'*n)
    for c in range(n, 0, -1):
        f *= c
        if c >= 2 and True == show:
            print(c, end=' x ')
        elif c == 1 and True == show:
            print(c, end=' = ')
    return f


print(fatorial(15, show=True))
help(fatorial)
