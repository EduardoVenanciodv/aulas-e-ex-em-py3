matriz = [[], [], []]
cont = 0
for c in range(0, 12):
    if c <= 2:
        matriz[0].append(int(input(f'Digite um valor para [0, {cont}]:')))
        cont += 1
    elif c <= 5:
        if c == 3:
            cont = 0
        matriz[1].append(int(input(f'Digite um valor para [1, {cont}]:')))
        cont += 1
    elif c <= 8:
        if c == 6:
            cont = 0
        matriz[2].append(int(input(f'Digite um valor para [2, {cont}]:')))
        cont += 1
print('_-_'*10)
for i in matriz[0]:
    print(f'[{i:^5}]', end=' ')
print()
for i in matriz[1]:
    print(f'[{i:^5}]', end=' ')
print()
for i in matriz[2]:
    print(f'[{i:^5}]', end=' ')
