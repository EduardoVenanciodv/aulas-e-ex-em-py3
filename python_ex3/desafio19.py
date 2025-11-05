aluno = dict()
aluno['Nome'] = str(input('Nome:'))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}:'))
if aluno['Média'] >= 6:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] < 6:
    aluno['Situação'] = 'Reprovado'
for a, r in aluno.items():
    print(f'{a} é igual a {r}.')
print(aluno)