nomenum = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesses', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número de 0 ao 20: '))
while True:
    if n < 0 or n > 20:
        n = int(input('Tente novamente. Digite um número de 0 ao 20: '))
    elif n >= 0 or n <= 20:
        print(f'Voce digitou o número \033[34m{nomenum[n]}\033[m.')
        r = str(input('Você quer ver mais números (\033[32mSim\033[m/\033[31mNão\033[m)?')).upper().strip()[0]
        if r == 'S':
            n = int(input('Digite um novo número de 0 ao 20: '))
        elif r == 'N':
            break
print('Fim')
