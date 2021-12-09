import os
import getpass

lista_arquivos = []
lista_extensoes = []

user = getpass.getuser()

pasta = 'C:/Users/{0}/Downloads/arquivos'.format(user)  #configurável
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        lista_arquivos.append(arquivo)
        #print(os.path.join(diretorio, arquivo))
        lista_extensoes.append('x')

#print(user)
#print(lista_arquivos)
