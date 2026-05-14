
def leia_dinheiro(msg):
    while True:
        try:
            p = float(input(msg).replace(",", "."))
            break
        except (ValueError, TypeError):
            print('\033[031mErro: Tivemos um problema no valor inserido!!\033[m')
        except KeyboardInterrupt:
            print('\n\033[031mErro: Usuário desistiu de informar os dados!!\033[m')
            p = 'zero'
            break
    return p

