from time import sleep
def maior(*valor):
    print('__'*25)
    print('Analisando os valores passados...')
    num = 0
    for c, n in enumerate(valor):
        if c == 0:
            num = n
        else:
            if num <= n:
                num = n
        print(n, end=' ')
        sleep(0.4)
    print(f'Foram informados {len(valor)} valores ao todo.')
    print(f'O maior valor informado foi {num}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
