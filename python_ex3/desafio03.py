from random import randint
maiorvl = menorvl = i = 0
aleatorio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram : ', end='')
for c in aleatorio:
    print(f'{c}',  end=' ')
    if i == 0:
        menorvl = c
    if maiorvl < c:
        maiorvl = c
    if menorvl > c:
        menorvl = c
    i = 1
print(f'\nO maiora valor sorteado foi : {maiorvl}')
print(f'O menor valor sorteado foi : {menorvl}')
