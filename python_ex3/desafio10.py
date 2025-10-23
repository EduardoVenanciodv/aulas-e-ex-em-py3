lista = []
saida = ''
while saida != 'N':
    num = lista.append(int(input('Digite um numero:')))
    saida = str(input('Quer continuar (S/N)?')).upper().strip()[0]
print('_+_'*20)
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente{lista}')
if 5 in lista:
    print(f'O 5 faz parte da lista!')
else:
    print('O 5 não está na lista!')
