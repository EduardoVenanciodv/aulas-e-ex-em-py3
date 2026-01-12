
def leiaint(n1):
    """

    :param n1: le um numero inteiro
    :return: Retonar o valor do n1 para n
    """
    n1 = input('Digite um número:')
    if n1.isdigit():
        n1 = int(n1)
    while True:
        if isinstance(n1, int):
            return n1
        else:
            print('\033[031mErro!! Digite um número inteiro valido\033[m')
            n1 = leiaint('Digite um número:')


print('__'*15)
n = leiaint('Digite um número:')
print(f'Você acabou de digitar o número {n}.')

