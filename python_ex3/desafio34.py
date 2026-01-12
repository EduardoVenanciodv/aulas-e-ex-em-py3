
def notas(* n, sit=False):
    planilha = dict()
    planilha['total'] = len(n)
    cont = 0
    total = 0
    for c in n:
        if cont == 0:
            menor = c
            maior = c
            cont += 1
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor = c
        total += c
    mediaT = total / len(n)
    planilha['Maior nota'] = maior
    planilha['Menor nota'] = menor
    planilha['Media'] = mediaT
    if mediaT == 10 and True is sit:
        planilha['Situação'] = 'Perfeita'
    if 8.5 <= mediaT < 10 and True is sit:
        planilha['Situação'] = 'Muito Boa'
    if 7 <= mediaT < 8.5 and True is sit:
        planilha['Situação'] = 'Boa'
    if 5 <= mediaT < 7 and True is sit:
        planilha['Situação'] = 'Mediana'
    if 0 <= mediaT < 5 and True is sit:
        planilha['Situação'] = 'Ruim'
    return planilha


resp = notas(3, 2, 4, 1, sit=True)
print(resp)
