from datetime import date

def voto(a):
    idade = data.year - a
    if idade < 16:
        print(f'Com {idade} anos: Não vota!')
    elif idade == 16 or idade == 17 or idade > 69:
        print(f'Com {idade} anos: Voto opcional!')
    else:
        print(f'Com {idade} anos: Voto obrigatório!!')


print('__'*13)
data = date.today()
voto(int(input('Que ano você nasceu?')))
