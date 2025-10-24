maior_valor = menor_valor = valor = 0
lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite um número para posição {cont}:')))
    if cont == 0:
        maior_valor = lista[cont]
        menor_valor = lista[cont]
    else:
        if maior_valor < lista[cont]:
            maior_valor = lista[cont]
        if menor_valor > lista[cont]:
            menor_valor = lista[cont]
print(f'Você digitou os valores :{lista}')
print(f'O maior valor da lista é {maior_valor} que está na posição:', end='')
for p, v in enumerate(lista):
    if v == maior_valor:
        print(p, end='... ')
print(f'\nO menor valor da lista é {menor_valor} que está na posição:', end='')
for p, v in enumerate(lista):
    if v == menor_valor:
        print(p, end='... ')
