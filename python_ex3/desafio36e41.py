from ex36ao41.utilidadescev import moeda, dado

p = dado.leia_dinheiro('Digite um valor:$')

if p == 'zero':
    print('\033[031mPrograma encerrado!\033[m')
else:
    print(f'A metade do valor {moeda.moeda(p)} é {moeda.metade(p, True)}')
    print(f'O dobro do valor {moeda.moeda(p)} é {moeda.dobro(p, True)}')
    print(f'O aumento de 10%, temos {moeda.aumento(p, 10, True)}')
    print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
    moeda.resumo(p, 80, 35)
