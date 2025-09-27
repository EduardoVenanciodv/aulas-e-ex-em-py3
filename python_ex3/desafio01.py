nomenum = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesses', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número de 0 ao 20: '))
while True:
    if n < 0 or n > 20:
        n = int(input('Tente novamente. Digite um número de 0 ao 20: '))
    else:
        break

print(f'Voce digitou o número {nomenum[n]}')
