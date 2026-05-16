from projctsystem44.system import *


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def ler_arquivo(nome):
    try:
        a = open(nome, 'r')
    except:
        print('Erro não foi possivel ser lido')
    else:
        cabeçalho('Lista de pessoas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{cor("*", "roxo"):<10}{dado[0]:<27}{dado[1]:>3} Anos')
    finally:
        a.close()


def adicionar_dados(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro: Não foi possivel adicionar os dados')
    else:
        try:
            a.write(f'\n{nome};{idade}')
        except:
            print('Erro não foi possivel adicionar os dados')
        else:
            print(f'Os dados de {cor(nome, "amarelo")} foram adicionados')
