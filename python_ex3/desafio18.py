turma901 = []
while True:
    nome_aluno = str(input('Nome do Aluno:'))
    nota1 = float(input('Digite  primeira nota:'))
    nota2 = float(input('Digite  segunda nota:'))
    media = (nota1 + nota2) / 2
    turma901.append([nome_aluno, [nota1, nota2], media])
    continuar = str(input('Quer continuar (S/N)?')).upper().strip()[0]
    if continuar == 'N':
        print('**'*15)
        break
print(f'{"N^":<4} Nome {"Media":>14}')
for n, c in enumerate(turma901):
    print(f'{n:<4} {c[0]:<8} {c[2]:>10}')
while True:
    print('--'*15)
    res = int(input('Digite o número do aluno, para saber as notas dele (Interromper 999):'))
    if res == 999:
        break
    if res <= len(turma901) - 1:
        print(f'Notas do {turma901[res][0]} são {turma901[res][1]}.')
print('Finalizado...')
