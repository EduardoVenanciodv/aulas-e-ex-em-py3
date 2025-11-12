from datetime import date
cadastro = dict()
ano = date.today()
cadastro['Nome'] = str(input('Digite seu nome:'))
nascimento = int(input('Digite o seu ano de nascimento: '))
cadastro['Idade'] = ano.year - nascimento
cadastro['CTPS'] = int(input('Digite o número da sua carteira de trabalaho (0 se você não tiver):'))
if cadastro['CTPS'] != 0:
    cadastro['Contrato'] = int(input('Ano de contratação:'))
    cadastro['Sálario'] = float(input('Digite seu sálario:'))
    cadastro['Aposentadoria'] = (cadastro['Contrato'] - nascimento) + 35
print('=-'*20)
for k, v in cadastro.items():
    print(f'  - {k} tem o valor {v}')
