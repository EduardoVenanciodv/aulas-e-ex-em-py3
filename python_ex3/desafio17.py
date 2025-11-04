from random import randint
from time import sleep
sorteio = []
final = []
total = 0
print('='*40)
print(f'{"Jogo da Mega Sena":^40}')
print('='*40)
x = int(input('Quantos jogos você quer que eu sorteie?'))
while total <= x:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in sorteio:
            sorteio.append(num)
            cont += 1
        if cont == 6:
            break
    sorteio.sort()
    final.append(sorteio[:])
    sorteio.clear()
    total += 1
print(f'{" Sorteando":*>15} {x} {"Jogos ":*<15}')
for i in range(0, x):
    print(f'Jogo {i+1}: {final[i]}.')
    sleep(1)
print(f'{" =":*>11} {"Boa Sorte"} {"= ":*<11}')
