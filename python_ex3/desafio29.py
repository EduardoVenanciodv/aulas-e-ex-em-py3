from random import randint
from time import sleep
numeros = list()


def sorteio(*valor_sort):
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        print(valor_sort[c], end=' ')
        sleep(0.4)
        numeros.append(valor_sort[c])
    print('PRONTO!')


sorteio(randint(1, 10), randint(1, 10), randint(1, 10),
        randint(1, 10), randint(1, 10))


def somaPar(valor_list):
    num = 0
    for s in valor_list:
        if s % 2 == 0:
            num += s
    print(f'Somando os valores pares de {numeros}, temos {num}.')


somaPar(numeros)
