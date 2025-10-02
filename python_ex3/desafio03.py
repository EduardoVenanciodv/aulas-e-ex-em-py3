from random import randint
n = n1 = n2 = n3 = n4 = maiorvl = menorvl = 0

for c in range(0, 5):
    aleatorio = randint(1, 10)
    if c == 0:
        n = aleatorio
        menorvl = aleatorio
    if c == 1:
        n1 = aleatorio
    if c == 2:
        n2 = aleatorio
    if c == 3:
        n3 = aleatorio
    if c == 4:
        n4 = aleatorio
    if maiorvl < aleatorio:
        maiorvl = aleatorio
    if menorvl > aleatorio:
        menorvl = aleatorio
numbers = (n, n1, n2, n3, n4)
print(f'Os valores sorteados foram : {numbers}')
print(f'O maiora valor sorteado foi : {maiorvl}')
print(f'O menor valor sorteado foi : {menorvl}')
