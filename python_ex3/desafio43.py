import urllib.request

try:
    site = urllib.request.urlopen("https://www.detran.rj.gov.br")
except:
    print('Não consegui me conectar')
else:
    print('Conectado com sucesso')
