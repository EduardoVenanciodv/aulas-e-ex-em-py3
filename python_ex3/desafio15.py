matriz = []
part = []
part1 = []
part2 = []
cont = cont1 = cont2 = 0
for c in range(0, 12):
    if c <= 2:
        part.append(int(input(f'Digite um valor para [0, {cont}]')))
        cont += 1
    elif c <= 5:
        part1.append(int(input(f'Digite um valor para [1, {cont1}]')))
        cont1 += 1
    elif c <= 8:
        part2.append(int(input(f'Digite um valor para [2, {cont2}]')))
        cont2 += 1
    if c == 8:
        matriz.append(part[:])
        matriz.append(part1[:])
        matriz.append(part2[:])
        for i in range(0, 3):
            print(f'{matriz[i]}')
