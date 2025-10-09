palavras = ('CADERNO', 'MESA', 'MOUSE', 'TECLADO', 'CAMISA',
            'MONITOR', 'CELULAR', 'TELEFONE', 'BICICLETA', 'DEUS')
print('-_-'*12)
print(f'{'VOGAIS':^36}')
print('-_-'*12)
for c in palavras:
    vogais = ' '
    cont = tamanho = 0
    print(f'\nNa palavra {c} Temos ', end='')
    while True:
        tamanho = len(c)
        separador = c[cont]
        if separador.upper() in 'AEIOU':
            print(separador, end=' ')
        cont += 1
        if cont == tamanho:
            break
