# https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?

from os import PRIO_PGRP, pipe
import requests
from bs4 import BeautifulSoup

print('########################################################## \n')

print('----- RASTREADOR DE ENCOMENDAS - CORREIOS BRASIL ----- \n')

print('########################################################## \n')

codigo = input('Digite o numero de rastreio: \n')

req = requests.post(url='https://www2.correios.com.br/sistemas/rastreamento/ctrl/ctrlRastreamento.cfm?',data={'objetos':codigo})
soup = BeautifulSoup(req.text, 'html.parser')
texto = soup.find(id='UltimoEvento').strong.text
data = soup.find(id='UltimoEvento').text.split()[-1]


print(f'Status - {texto}')
print(f'Data - {data}')
print(f'Objetos - {codigo}')