grupo = [['Fabio', 42], ['Lucio', 56], ['Luiz', 25], ['Clara', 21]]
print(grupo[3][0])

for pessoas in grupo:
    print(f'{pessoas[0]} tem {pessoas[1]} anos.')

dados = list()
pessoas1 = list()
for n in range(0, 4):
    dados.append(str(input('Digite seu nome:')))
    dados.append(int(input('Digite sua idade:')))
    pessoas1.append(dados[:])
    dados.clear()
print(pessoas1)

contmaior = contmenor = 0
for i in pessoas1:
    if i[1] >= 18:
        print(f'{i[0]} é maior de idade.')
        contmaior += 1
    else:
        print(f'{i[0]} é  menor de idade.')
        contmenor += 1

print(f'Tem {contmaior} pessoas maiores de idade e {contmenor} menor de idade.')
