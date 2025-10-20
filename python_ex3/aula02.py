lista = [2, 9, 5, 7]
lista[2] = 3
lista.append(10)
lista.sort(reverse=True)
lista.insert(1, 6)
lista.pop(3)
if 1 in lista:
    lista.remove(1)
else:
    print('Não existe 1 na lista.')
print(lista)
print(f'Essa lista contem {len(lista)} elementos.')

num = list()
num.append(4)
num.append(2)
num.append(1)
num.append(7)

for c, n in enumerate(num):
    print(f'Na posição {c} está o número {n}!')

valores = []

for cont in range(0, 5):
    valores.append(int(input('Digite um números.')))
print(valores)

