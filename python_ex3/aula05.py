def contador(i, f, p):
    """
    -> Faz um contagem mostra na tela
    :para i: valor inicial da contagem
    :para f:valor final da contagem
    :para p:valor de cada passo que a contagem vai ter
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('Fim')


contador(5, 61, 2)
help(contador)
def soma(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :para a:Primeiro valor
    :para b:Segundo valor
    :para c:Terceiro valor

    """
    s = a + b + c
    '''print(f'A soma vale {s}')'''
    return s


r2 = soma(3, 5, 2)
r3 = soma(5, 3)
help(soma)
print(f'A soma dos valores é de {r2} e {r3}')


def test(b):
    global a
    a = 5
    b += 2
    c = 1
    print(f'O a local vale {a}')
    print(f'O b local vale {b}')
    print(f'O c local vale {c}')


a = 2
test(a)
print(f'O a global vale {a}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'O resultados doas fatorais é {f1}, {f2} e {f3}')

