lista = []
lista_2 = []
lista_3 = []
saida = ''
while True:
    lista.append(int(input('Digite um número: ')))
    saida = str(input('Quer continuar (S/N)?')).upper().strip()[0]
    if saida in 'N':
        break
for r in lista:
    if r % 2 == 0:
        lista_2.append(r)
    else:
        lista_3.append(r)
print(f'Primeira lista completa: {lista}\nSegunda lista só com números pares: {lista_2}'
      f'\nTerceira lista só com ímpars: {lista_3}')
