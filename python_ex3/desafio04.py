n1 = n2 = n3 = n4 = nine = pares = cont = 0
posic3 = ' '
n12 = int(input('Digite um numero:'))
n23 = int(input('Digite o segundo numero:'))
n34 = int(input('Digite o terceiro numero:'))
n45 = int(input('Digite o quarto numero:'))
num = (n12, n23, n34, n45)
if num[0]:
    if num[0] % 2 == 0:
        pares += 1
    if num[0] == 9:
        nine += 1
    if num[0] == 3:
        posic3 = 'Primeira posição'
        cont += 1
if num[1]:
    if num[1] % 2 == 0:
        pares += 1
    if num[1] == 9:
        nine += 1
    if num[1] == 3 and cont == 0:
        posic3 = 'Segunda posição'
        cont += 1
if num[2]:
    if num[2] % 2 == 0:
        pares += 1
    if num[2] == 9:
        nine += 1
    if num[2] == 3 and cont == 0:
        posic3 = 'Terceira posição'
        cont += 1
if num[3]:
    if num[3] % 2 == 0:
        pares += 1
    if num[3] == 9:
        nine += 1
    if num[3] == 3 and cont == 0:
        posic3 = 'Quarta posição'
        cont += 1
print(f'Sua tupla: {num}')
if nine == 0:
    print(f'O valor 9 não apareceu nenhuma vez')
elif nine > 0:
    print(f'O valor 9 apareceu {nine} vez(es).')
if num[0] == 3 or num[1] == 3 or num[2] == 3 or num[3] == 3:
    print(f'O valor 3 apareceu na {posic3}.')
else:
    print(f'O valor 3 não apareceu em nenhuma posição.')
print(f'Foram digitados {pares} par(es).')
