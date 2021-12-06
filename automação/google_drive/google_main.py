# -*- coding: UTF-8 -*-
from googleapiclient.http import MediaFileUpload
from google_facilitador import Create_Service

CLIENT_SECRET_FILE = 'google_drive\client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#print(dir(service))

id_da_pasta_destino = '17mByQE6Hkzk9xEGm6gwnW5SsbOaMW6_J'                               #define a pasta de destino do drive
arquivos_para_upload = ['WhatsApp Image 2021-12-02 at 07.47.50.jpeg', 'glpi.csv']                   #nome dos documntos.extensão
tipos_dos_arquivos = ['image/jpg', 'text/csv']                                                     #tipo de extensão 

caminho_de_busca = 'C:/Users/User/Downloads'

#try:

for nome_arquivo, mime_type in zip(arquivos_para_upload, tipos_dos_arquivos):
    file_meta = {
        'name' : nome_arquivo,
        'parents' : [id_da_pasta_destino]
    }

    media = MediaFileUpload('{0}/{1}'.format(caminho_de_busca, nome_arquivo), mimetype=mime_type)      #busca onde o arquivo deve estar

    service.files().create(
        body = file_meta,
        media_body = media,
        fields = 'id'
    ).execute()


''' #cria pasta
backup = ['belga']

file_meta = {
    'name' : backup,
    'mimeType' : 'application/vnd.google-apps.folder',
    #parents : []
}

service.files().create(body=file_meta).execute()
'''