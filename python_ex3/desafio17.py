from random import randint
from time import sleep
sorteio = []
print('='*40)
print(f'{"Jogo da Mega Sena":^40}')
print('='*40)
x = int(input('Quantos jogos você quer que eu sorteie?'))
print(f'{" Sorteando":*>15} {x} {"Jogos ":*<15}')
for i in range(0, x):
    for c in range(0, 6):
        num = randint(0, 60)
        sorteio.append(num)
        if c == 5:
            print(f'Jogo {i+1}: {sorteio}.')
            sleep(1)
            sorteio.clear()
print(f'{" =":*>11} {"Boa Sorte"} {"= ":*<11}')
