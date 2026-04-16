
def notas(* n, sit=False):
    """"
    -->Função para analisar todas as notas e situação dos alunos
    :param n: recebe uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve mostra a situção do aluno
    :return : dicionário com várias informções sobre a situação da turma
    """
    planilha = dict()
    planilha['total'] = len(n)
    planilha['Maior nota'] = max(n)
    planilha['Menor nota'] = min(n)
    planilha['Media'] = sum(n) / len(n)
    if sit:
        if planilha['Media'] == 10:
            planilha['Situação'] = 'Perfeita'
        if 8.5 <= planilha['Media'] < 10:
            planilha['Situação'] = 'Muito Boa'
        if 7 <= planilha['Media'] < 8.5:
            planilha['Situação'] = 'Boa'
        if 5 <= planilha['Media'] < 7:
            planilha['Situação'] = 'Mediana'
        if 0 <= planilha['Media'] < 5:
            planilha['Situação'] = 'Ruim'
    return planilha


resp = notas(4, 2, 8, 6, sit=True)
print(resp)
#help(notas)
