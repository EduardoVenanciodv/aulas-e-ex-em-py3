
try:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valors: '))
    r = n1 / n2
except (ValueError, TypeError):
    print('Tivemos um problema nos dados que você inseriu.')
except ZeroDivisionError:
    print('Nenhum valor não pode ser dividido por zero!')
except KeyboardInterrupt:
    print('O usuário não informou todos os dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__} ')
else:
    print(f'O resultado da divisão é {r:.1f}')
finally:
    print('Até logo.')




