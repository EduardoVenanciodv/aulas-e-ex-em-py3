maior_valor = menor_valor = valor = 0
lista = []
maior_cont = []
menor_cont = []
for cont in range(0, 5):
    lista.append(int(input('Digite um número:')))
    valor = lista[cont]
    if cont == 0:
        maior_valor = valor
        menor_valor = valor
    if maior_valor <= valor:
        if maior_valor < valor:
            maior_cont = []
            maior_cont.append(cont)
        elif maior_valor == valor:
            maior_cont.append(cont)
        maior_valor = valor
    if menor_valor >= valor:
        if menor_valor == valor:
            menor_cont.append(cont)
        elif menor_valor > valor:
            menor_cont = []
            menor_cont.append(cont)
        menor_valor = valor
print(f'Você digitou os valores :{lista}')
print(f'O(s) maior(es) valor(es) fo(ram) {maior_valor}, na(s) posiç(ões):', end=' ')
for ma in maior_cont:
    print(f'{ma}..', end=' ')
print(f'\nO(s) menor(es) valor(es) fo(ram) {menor_valor}, na(s) posiç(ões):', end=' ')
for me in menor_cont:
    print(f'{me}..', end=' ')
