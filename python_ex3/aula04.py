def mensagem(msg):
    print('--'*20)
    print(msg)
    print('--'*20)

mensagem('Sistema')
mensagem('de')
mensagem('alunos')

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + b = {s}')


soma(b=2, a=5)
soma(4, 12)

def dobro(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 4, 1, 0, 5]
dobro(valores)
print(valores)

def soma1(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma1(3, 6, 2)
soma1(7, 1)
