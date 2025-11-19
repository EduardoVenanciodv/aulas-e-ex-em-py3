from operator import neg
from time import sleep
def contador(a, b, c):
    print('-='*20)
    if a < b:
        print(f'Contatem de {a} ate {b} de {c} em {c}.')
        for x in range(a, b+1, c):
            print(x, end=' ')
            sleep(0.3)
        print('FIM!')
    elif a > b:
        if c == 0:
            c += 1
        print(f'Contatem de {a} ate {b} de {c} em {c}.')
        if neg(c):
            for x in range(a, b-1, c):
                print(x, end=' ')
                sleep(0.3)
        if c > neg(c):
            c = neg(c)
            for x in range(a, b-1, c):
                print(x, end=' ')
                sleep(0.3)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Inicio:')), int(input('Fim:')), int(input('Passo:')))

