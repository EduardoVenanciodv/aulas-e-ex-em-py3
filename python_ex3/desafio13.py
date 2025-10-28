dados = list()
pessoas = list()
nomel = list()
nomep = list()
contp = cont = maisp = maisl = 0
while True:
    dados.append(str(input('Digite seu nome:')))
    dados.append(int(input('Digite seu peso:KG ')))
    pessoas.append(dados[:])
    dados.clear()
    contp += 1
    continuar = str(input('Quer continuar (S/N)?')).upper().strip()[0]
    if continuar == 'N':
        for pl in pessoas:
            if cont == 0 and pl[1]:
                maisp = pl[1]
                nomep.append(pl[0])
                maisl = pl[1]
                nomel.append(pl[0])
            elif pl[1]:
                if maisp <= pl[1]:
                    if maisp != pl[1]:
                        nomep.clear()
                    maisp = pl[1]
                    nomep.append(pl[0])
                if maisl >= pl[1]:
                    if maisl != pl[1]:
                        nomel.clear()
                    maisl = pl[1]
                    nomel.append(pl[0])
            cont = 1
        break
print(f'Ao todo cadastrou {contp} pessoas.')
print(f'O maior peso é {maisp:.1f}KG. Peso de {nomep}.')
print(f'O menor peso é {maisl:.1f}KG. Peso de {nomel}.')
