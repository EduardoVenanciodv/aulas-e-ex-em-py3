from urllib import error
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com')
except urllib.error.URLError:
    print('Não consegui me conectar')
else:
    print('Conectado com sucesso')
