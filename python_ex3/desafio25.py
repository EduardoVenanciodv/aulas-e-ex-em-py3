def m2(largura, comprimento):
    x2 = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {x2}m2')


print(f'{"Controle de terrenos":^25}')
print('-'*25)
m2(float(input('Lagura (m):')), float(input('Comprimento (m):')))
