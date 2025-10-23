lista = []
lista.append(str(input('Digite um expressão: ')))
cont_open = cont_closing = 0
for c in lista[0][:]:
    if c == '(':
        cont_open += 1
    elif c == ')':
        cont_closing += 1
if cont_closing == cont_open:
    print('Sua expressão está válida.')
else:
    print('Sua expressão está errada.')
