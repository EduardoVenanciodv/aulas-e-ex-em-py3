
def leiaint(msg):
    """
    :param n1: le um numero inteiro
    :param valor: Recebe o valor de n1 quando o n1 for numeric
    :param ok: O 'ok' por padrão é 'False'.
               Enquanto o 'ok' não se torna 'True',
               o repetidor while não irar pausar
    :return: Retonar o valor do da variavel 'valor' para n
    """
    ok = False
    valor = 0
    while True:
        n1 = str(input(msg))
        if n1.isnumeric():
            valor = int(n1)
            ok = True
        else:
            print('\033[031mErro!! Digite um número inteiro valido\033[m')
        if ok:
            break
    return valor


print('__'*15)
n = leiaint('Digite um número:')
print(f'Você acabou de digitar o número {n}.')
