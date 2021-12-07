import os

lista_arquivos = []
lista_extensoes = []

pasta = 'C:/Users/User/Downloads/arquivos'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        lista_arquivos.append(arquivo)
        #print(os.path.join(diretorio, arquivo))
        lista_extensoes.append('x')
