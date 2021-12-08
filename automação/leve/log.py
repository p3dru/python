'''try:
    nome_arquivo = 'log.txt'
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write('\n12345')
        arquivo.write('\nxcvb')
except FileNotFoundError:
    arquivo = open('google_drive/{0}'.format(nome_arquivo), 'w+')
    arquivo.write('Arquivo criado pois não existia')
arquivo.close()
'''

import os
from datetime import datetime

def verificar_existencia(mensagem):
    caminho = ''
    arquivo = caminho + '/log.txt'
    data_e_hora = datetime.now()
    data_e_hora_texto = data_e_hora.strftime('%d/%m/%Y %H:%M')

    if not os.path.exists(caminho):
        os.makedirs(caminho)
    
    if not os.path.exists(arquivo):
        with open(arquivo, 'a') as arquivo:
            arquivo.write(f'Arquivo de log criado em {data_e_hora_texto}')
            arquivo.write(mensagem + f' ({data_e_hora_texto})')
    else:
        with open(arquivo, 'a') as arquivo:    
            arquivo.write(mensagem + f' ({data_e_hora_texto})')


    return arquivo

