aluno = dict()
aluno['Nome'] = str(input('Nome:'))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}:'))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
elif aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
print('=-'*25)
for a, r in aluno.items():
    print(f'{"-":>3} {a} é igual a {r}.')
