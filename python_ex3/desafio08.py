lista = []
continuar = 'S'
while continuar != 'N':
    valor = 0
    valor = int(input('Digite um número:'))
    if valor in lista:
        print('Valor duplicado. Não foi adicionado!')
    else:
        print('Valor adicionado com sucesso!')
        lista.append(valor)
    continuar = str(input('Quer continuar (S/N)?')).upper().strip()[0]
lista.sort()
print('-='*20)
print(f'Você digitou :{lista}')
