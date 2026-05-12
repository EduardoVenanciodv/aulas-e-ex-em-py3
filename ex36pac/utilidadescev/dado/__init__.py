
def leiadinheiro(p):
    print(p, end='')
    p = input().replace(",", ".")
    while True:
        try:
            float(p)
            p = float(p)
            break
        except ValueError:
            print(f'\033[031mErro o valor "{p}" é invalido!!\033[m:')
            p = input('Digite um valor:$').replace(",", ".")
    return p

