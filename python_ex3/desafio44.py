from projctsystem44 import system
from time import sleep

while True:
    resposta = system.menu(['Ver pessoas cadastradas',
                            'Cadastra nova pessoa',
                            'Sair do sistema'])
    if resposta == 1:
        system.cabeçalho('Opção 2')
        sleep(0.6)
    elif resposta == 2:
        system.cabeçalho('Opção 2')
        sleep(0.6)
    elif resposta == 3:
        system.cabeçalho('Saindo do sistema... Até logo!')
        sleep(0.6)
        break




