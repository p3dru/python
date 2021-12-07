# -*- coding: UTF-8 -*-
from googleapiclient.http import MediaFileUpload
from google_facilitador import Create_Service
from verificar_arquivos_na_pasta import lista_arquivos, lista_extensoes

CLIENT_SECRET_FILE = './rotina/client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#print(dir(service))

id_da_pasta_destino = '1Xlwjb520zWWrAtv4yZw6mENAzVoQ60Zy'                                           #define a pasta de destino do drive
#arquivos_para_upload = ['glpi.csv', 'Cadastro_Usuario_Externo_Termo_Declaracao_Concordancia_e_Veracidade']                #nome dos documntos.extensão
#ipos_dos_arquivos = ['application/pdf', 'application/pdf']                                                      #tipo de extensão não necessário

#basta fazer um for pra pegar todos os documentos da pasta e dar um rep


caminho_de_busca = 'C:/Users/User/Downloads/arquivos'

#try:

for nome_arquivo, mime_type in zip(lista_arquivos, lista_extensoes):#, tipos_dos_arquivos):#, tipos_dos_arquivos):
    file_meta = {
        'name' : nome_arquivo,
        'parents' : [id_da_pasta_destino]
    }

    media = MediaFileUpload('{0}/{1}'.format(caminho_de_busca, nome_arquivo))#, mimetype=mime_type)      #busca onde o arquivo deve estar, (configurável)

    service.files().create(
        body = file_meta,
        media_body = media,
        fields = 'id'
    ).execute()

'''
#cria pasta
backup = ['belga']

file_meta = {
    'name' : backup,
    'mimeType' : 'application/vnd.google-apps.folder',
    #parents : []
}

service.files().create(body=file_meta).execute()
'''
print(lista_arquivos)