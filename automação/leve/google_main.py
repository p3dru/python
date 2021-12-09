# -*- coding: UTF-8 -*-
from googleapiclient.http import MediaFileUpload
from google_facilitador import Create_Service
from verificar_arquivos_na_pasta import lista_arquivos, lista_extensoes, pasta
from log import verificar_existencia

def criar_pasta():
    #criar e pegar id da pasta
    backup = 'Backup Belga'                                                                          #nome configurável

    file_meta = {
        'name' : backup,
        'mimeType' : 'application/vnd.google-apps.folder',
        #parents : []
    }
    arquivo = service.files().create(body=file_meta,
                                    fields='id').execute()

    drive_pasta = arquivo.get('id')
    #print(arquivo.get('id'))
    return drive_pasta



CLIENT_SECRET_FILE = 'client_secret.json'                                           #busca o client file
API_NAME = 'drive'                                                                                   #mostra a api é utilizada
API_VERSION = 'v3'                                                                                   #versão da api
SCOPES = ['https://www.googleapis.com/auth/drive']                                                   #escopo da api

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)                          #cria o serviço

#print(dir(service))


id_da_pasta_destino = criar_pasta()                                                                  #define a pasta de destino do drive
#arquivos_para_upload = ['glpi.csv', 'Cadastro_Usuario_Externo_Termo_Declaracao_Concordancia_e_Veracidade']                #nome dos documntos.extensão
#ipos_dos_arquivos = ['application/pdf', 'application/pdf']                                                      #tipo de extensão não necessário

#basta fazer um for pra pegar todos os documentos da pasta e dar um rep


caminho_de_busca = pasta                                                                             #caminho de busca para vasculhar os arquivos (CONFIGURÁVEL)

#try:
lista_falhas = []

for nome_arquivo, mime_type in zip(lista_arquivos, lista_extensoes):#, tipos_dos_arquivos):#, tipos_dos_arquivos):
    file_meta = {
        'name' : nome_arquivo,
        'parents' : [id_da_pasta_destino]
    }
                    #buscar uma forma de realizar o upload forçado
    try:
        media = MediaFileUpload('{0}/{1}'.format(caminho_de_busca, nome_arquivo))#, mimetype=mime_type)  #busca onde o arquivo deve estar, (configurável)
        
        service.files().create(
            body = file_meta,
            media_body = media,
            fields = 'id'
        ).execute()

        mensagem = f'\nFeito Upload do arquivo {nome_arquivo}'
        verificar_existencia(mensagem)
    except:
        mensagem = f'Não foi possível realizar o Upload do arquivo {nome_arquivo}'
        
        


#FALTA RESOLVER O PROBLEMA DE CRIAR VÁRIAS PASTAS NO DRIVE
#try catch para cada erro de upload, insistir no upload com while
#retirar cada arquivo dado upload na lista (testar)
#inserir um contador de quantos arquivos x devem existir no drive
#se não definir a pasta deixa no raiz




#print(lista_arquivos)
