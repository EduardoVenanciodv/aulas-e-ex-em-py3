lista = []
pos = final = primeiro = inicio = 0
for c in range(0, 5):
    num = int(input('Digite um número:'))
    if num > 5:
        print('Adicionado no final da lista')
        if final == 0:
            lista.append(num)
            abaixo = num
            primeiro = num
            final = 1
        if num > primeiro and final == 1:
            lista.append(num)
        elif num < abaixo and final == 1:
            lista.insert(lista.index(abaixo), num)
            abaixo = num
        elif num < primeiro and final == 1:
            lista.insert(lista.index(primeiro), num)
    else:
        if inicio == 0:
            inicio = 1
            lista.insert(0, num)
            menor = num
            valor_1 = num
        elif num < menor and inicio == 1:
            lista.insert(lista.index(menor), num)
            menor = num
        elif num > valor_1 and inicio == 1:
            lista.insert(lista.index(valor_1)+1, num)
            valor_1 = num
        elif num > menor and num < valor_1 and inicio == 1:
            lista.insert(lista.index(valor_1), num)
        print(f'Adicionado na posição: {lista.index(num)}')
print(lista)
