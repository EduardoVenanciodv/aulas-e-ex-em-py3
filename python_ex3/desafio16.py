matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maiorv = pares = 0
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um numero na posição [{l}, {c}]:'))
        matriz[l][c] = valor
        if valor % 2 == 0:
            pares += valor
        if l == 1 and c == 0:
            maiorv = valor
        else:
            if maiorv < valor and l == 1:
                maiorv = valor

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('=_'*15)
print(f'A soma dos pares é {pares}.')
print(f'A soma da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}.')
print(f'O maior valor da segunda linha é {maiorv}.')
