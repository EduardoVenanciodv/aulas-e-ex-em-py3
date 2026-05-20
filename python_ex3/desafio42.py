
def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Tivemos um problema no valor inserido. Digite um valor Inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31m\nErro: O usuário preferiu não digitar nenhum número.\033[m')
            return 0
        else:
            return valor


def leiareal(msg):
    while True:
        try:
            valor = float(input(msg).replace(",", "."))
        except (ValueError, TypeError):
            print('\033[31mErro: Problema no dado inserido. Digite um valor Real válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31m\nErro: Usuário não quis inserir os dados.\033[m')
            return 0
        else:
            return valor


inteiro = leiaint('Digite um valor inteiro: ')
real = leiareal('Digite um valor real: ')
print(f'O valor inteiro foi {inteiro} e o real foi {real:.2f}.')
