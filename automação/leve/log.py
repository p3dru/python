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


def verificar_existencia():
    caminho = 'google_drive'
    arquivo = caminho + '/log.txt'

    if not os.path.exists(caminho):
        os.makedirs(caminho)
    
    if not os.path.exists(arquivo):
        open(arquivo, 'w')
    else:
        with open(arquivo, 'a') as arquivo:
            arquivo.write('\nlog feito')


    return arquivo

verificar_existencia()
