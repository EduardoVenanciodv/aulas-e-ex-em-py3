num = []
par = []
impar = []
cont = 0
for c in range(0, 7):
    cont += 1
    valor = (int(input(f'Digite o {cont}^ número:')))
    if valor % 2 == 0:
        par.append(valor)
    elif valor % 2 == 1:
        impar.append(valor)
num.append(par[:])
num.append(impar[:])
par.sort(reverse=False)
impar.sort(reverse=False)
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores ímpares digitados foram: {impar}')
print(num)
