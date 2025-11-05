from random import randint
from time import sleep
jogadores = dict()
for num in range(1, 5):
    jogadores[f'Jogador{num}'] = randint(1, 6)
print('Valores Sorteado:')
for j, n in jogadores.items():
    print(f'{"O":>4} {j} tirou {n}')
    sleep(0.7)
print("Ranking dos jogadores:")
for c, l in enumerate(sorted(jogadores, key=jogadores.get, reverse=True)):
    print(f'{c+1:>4}^ lugar: foi {l} com {jogadores[l]}.')
    sleep(0.7)
