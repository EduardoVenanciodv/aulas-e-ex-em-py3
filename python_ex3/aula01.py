frutas = ('Banana', 'Maça', 'Morango', 'Kiwi', 'Melão')
print(frutas[1:4])

for comer in frutas:
    print(f'Eu vou comer {comer}')
print('-=-'*10)
for comida in range(0, len(frutas)):
    print(f'Eu gosto de: {comida} {frutas[comida]} ')
print('-=-'*10)
for pos, comer in enumerate(frutas):
    print(f'Eu vou comer {comer} que está na posição {pos}')

a = (3, 5, 2, 1, 'Fim')
b = (7, 3, 2, 8)
c = a + b
print(c)
