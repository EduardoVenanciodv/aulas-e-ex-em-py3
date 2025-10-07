palavras = ('CADERNO', 'MESA', 'MOUSE', 'TECLADO', 'CAMISA',
            'MONITOR', 'CELULAR', 'TELEFONE', 'BICICLETA', 'DEUS')
print('-_-'*12)
print(f'{'VOGAIS':^36}')
print('-_-'*12)
for c in palavras:
    vogais = ' '
    cont = tamanho = 0
    while True:
        tamanho = len(c)
        separador = c[cont]
        '''print(b)'''
        if separador == 'A' or separador == 'E' or separador == 'I' or separador == 'O' or separador == 'U':
            vogais += separador
        cont += 1
        if cont == tamanho:
            break
    print(f'Na palavra {c} Temos {vogais}')
