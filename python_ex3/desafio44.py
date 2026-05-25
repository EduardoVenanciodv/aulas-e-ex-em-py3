from projctsystem44.system import *
from projctsystem44.arquivo import *
from time import sleep

arq = 'dados.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas',
                     'Cadastra nova pessoa',
                     'Sair do sistema'])
    if resposta == 1:
        cabeçalho('Pessoas Cadastradas')
        ler_arquivo(arq)
        sleep(0.8)
    elif resposta == 2:
        cabeçalho('Novo Cadastro')
        nome = input(cor('Digite o nome:', 'amarelo'))
        idade = leiainteiro(cor('Digite a idade:', 'amarelo'))
        adicionar_dados(arq, nome, idade)
        sleep(0.6)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        sleep(0.6)
        break




