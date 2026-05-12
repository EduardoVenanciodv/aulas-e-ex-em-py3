from ex36pac.utilidadescev import moeda

p = float(input('Digite um valor: $'))

print(f'A metade do valor {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro do valor {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'O aumento de 10%, temos {moeda.aumento(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
moeda.resumo(p, 80, 35)


