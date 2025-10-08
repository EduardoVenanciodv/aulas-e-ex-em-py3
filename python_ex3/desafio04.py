pares = p = 0
num = (int(input('Digite um numero:')),
       int(input('Digite o segundo numero:')),
       int(input('Digite o terceiro numero:')),
       int(input('Digite o quarto numero:')))
print(f'Sua tupla: {num}')
if 9 in num:
    print(f'O valor 9 apareceu {num.count(9)} vez(es).')
else:
    print(f'O valor 9 não apareceu nenhuma vez')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}^ posição.')
else:
    print(f'O valor 3 não apareceu em nenhuma posição.')
for c in num:
    if c % 2 == 0:
        pares += 1
        print(f'({c})', end='')
    if c == num[3]:
        print(f' Esses número(s) são par(es). Foram digitados {pares} par(es).')
