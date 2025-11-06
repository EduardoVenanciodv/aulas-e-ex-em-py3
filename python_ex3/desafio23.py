cadastros = []
pessoa = {}
grupotot = media_idadetot = cont = contm = 0
while True:
    pessoa['nome'] = str(input('Nome:'))
    pessoa['sexo'] = str(input('Sexo (M/F): ')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    grupotot += 1
    cadastros.append(pessoa.copy())
    continuar = str(input('Quer continuar (S/N)?')).upper().strip()[0]
    if continuar == 'N':
        break
print('=-'*20)
print(f'- O grupo tem {grupotot} pessoas.')
for c in range(0, grupotot):
    media_idadetot += cadastros[c]['idade']
media_idadetot = media_idadetot / grupotot
print(f'- A média de idade é {media_idadetot:.0f}.')
print(f'- As mulheres cadastradas foram:', end=' ')
for c in range(0, grupotot):
    for p in cadastros[c]['sexo']:
        if p == 'F':
            print(f'{cadastros[c]["nome"]}', end=' ')
            contm = 1
if contm == 0:
    print('Nenhuma mulher cadastrada!', end=' ')
print('\n- Lista de pessoas que estão acima da média:\n')
for c in range(0, grupotot):
    if cadastros[c]['idade'] > media_idadetot:
        print(cadastros[c])
        print()
        cont = 1
if cont == 0:
    print('Não tem pessoas acima da média!')
