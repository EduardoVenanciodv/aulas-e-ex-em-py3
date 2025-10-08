produtos = ('Tang', 1,
            'Leite', 4.15,
            'Toddy', 7,
            'Banana', 3.56,
            'Pão', 7.70,
            'Tapioca', 5.70,
            'Farofa', 5)
texto = 'Listagem De Preços'
cont = 0
print('_'*60)
print(f'{texto:^60}')
print('_'*60)
for c in produtos:
    cont += 1
    if cont == 1:
        print(f'{c:.<50}', end='')
    elif cont == 2:
        cont = 0
        print(f'R$ {c:>6.2f}')
print('_'*60)
