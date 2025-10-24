lista = []
for c in range(0, 5):
    num = int(input('Digite um número:'))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print(f'O {num} foi adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Foi adicionado na posição {pos} da lista')
                break
            pos += 1
print(lista)
