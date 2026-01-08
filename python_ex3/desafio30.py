def voto(a):
    from datetime import date
    data = date.today().year
    idade = data - a
    if idade < 16:
        print(f'Com {idade} anos: Não vota!')
    elif 16 <= idade == 17 or idade > 69:
        print(f'Com {idade} anos: Voto opcional!')
    else:
        print(f'Com {idade} anos: Voto obrigatório!!')


print('__'*13)
voto(int(input('Que ano você nasceu?')))
