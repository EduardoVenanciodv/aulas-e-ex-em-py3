cadastros = []
pessoa = {}
media_idadetot = cont = contm = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome:'))
    while True:
        pessoa['sexo'] = str(input('Sexo (M/F): ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por Favor Digite Apenas (M) Ou (F)!')
    pessoa['idade'] = int(input('Idade: '))
    media_idadetot += pessoa['idade']
    cadastros.append(pessoa.copy())
    while True:
        continuar = str(input('Quer continuar (S/N)?')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('Erro! Por Favor Digite Apenas (S) Ou (N)!')
    if continuar == 'N':
        break
print('=-'*20)
print(f'- O grupo tem {len(cadastros)} pessoas.')
media_idadetot = media_idadetot / len(cadastros)
print(f'- A média de idade é {media_idadetot:.0f}.')
print(f'- As mulheres cadastradas foram:', end=' ')
for c in cadastros:
    for p in c['sexo']:
        if p == 'F':
            print(f'{c["nome"]}', end=' ')
            contm = 1
if contm == 0:
    print('Nenhuma mulher cadastrada!', end=' ')
print('\n- Lista de pessoas que estão acima da média:\n')
for c in cadastros:
    if c['idade'] >= media_idadetot:
        cont = 1
        for v, k in c.items():
            print(f'{v} == {k}', end='; ')
print()
if cont == 0:
    print('Não tem pessoas acima da média!')
print(f'{"<< Encerrado >>":^35}')
