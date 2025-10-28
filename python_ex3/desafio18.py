turma901 = []
aluno = []
notas = []
lista_nome = []
cont = 0
while True:
    nome_aluno = str(input('Nome do Aluno:'))
    lista_nome.append(nome_aluno)
    nota1 = float(input('Digite  primeira nota:'))
    notas.append(nota1)
    nota2 = float(input('Digite  segunda nota:'))
    notas.append(nota2)
    aluno.append(lista_nome[:])
    aluno.append(notas[:])
    turma901.append(aluno[:])
    aluno.clear()
    lista_nome.clear()
    notas.clear()

    continuar = str(input('Quer continuar (S/N)?')).upper().strip()[0]
    if continuar == 'N':
        print('**'*15)

        print(f'{"N^":<4} Nome {"Media":>14}')
        for c in turma901:
            media = (c[1][0] + c[1][1]) / 2
            nome_final = c[0][0]
            print(f'{cont:<4} {nome_final:<8} {media:>10}')
            cont += 1
        while True:
            print('--'*15)
            n_aluno = int(input('Digite o número do aluno, para saber as notas dele (Interromper 999):'))
            if n_aluno == 999:
                break

            else:
                print(f'Notas do {turma901[n_aluno][0]} são {turma901[n_aluno][1]}.')
        break
print('Finalizado...')
