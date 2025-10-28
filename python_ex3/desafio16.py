matriz = []
part = []
part1 = []
part2 = []
pares = []
cont = cont2 = maiorv = pares = 0
for c in range(0, 9):
    if c <= 2:
        valor = int(input(f'Digite um numero na posição [0, {c}]'))
        part.append(valor)
        if valor % 2 == 0:
            pares += valor
    elif c <= 5:
        valor = int(input(f'Digite um numero na posição [1, {cont}]'))
        part1.append(valor)
        if valor % 2 == 0:
            pares += valor
        if c == 3:
            maiorv = valor
        else:
            if maiorv < valor:
                maiorv = valor
        cont += 1
    elif c <= 8:
        valor = int(input(f'Digite um numero na posição [2, {cont2}]'))
        part2.append(valor)
        if valor % 2 == 0:
            pares += valor
        cont2 += 1
    if c == 8:
        matriz.append(part[:])
        matriz.append(part1[:])
        matriz.append(part2[:])
        for m in range(0, 3):
            print(f'{matriz[m]}')
print('=_'*15)
print(f'A soma dos pares é {pares}.')
print(f'A soma da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}.')
print(f'O maior valor da segunda linha é {maiorv}.')
