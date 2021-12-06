for x in range(50):
    try:
        nome_arquivo = 'log.txt'
        arquivo = open(nome_arquivo, 'r+')
        arquivo.write('xcvb')
    except FileNotFoundError:
        arquivo = open('./google_drive/{}'.format(nome_arquivo), 'w+')
        arquivo.writelines(u'Arquivo criado pois não existia')
arquivo.close()
