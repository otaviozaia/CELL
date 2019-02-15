#---------------ESSE MÓDULO COLETARÁ INFORMAÇÕES DO GOOGLE SHEETS E CRIARÁ NOTIFICAÇÕES NO TENDAEDU-------------------

from credenciais import*
from app import app
from flask import jsonify, request, render_template, redirect
import json
import requests
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

token_tenda = token_tenda_1

#essa rota será requisitada pelo script da planilha google "Ocurrences" >> https://docs.google.com/spreadsheets/d/1ILU2dxgAkumVD1P3yPt0zN5vZdG8SnWMFYxy47D4biQ/edit#gid=1703648543
@app.route("/ocorrencias")
def getOcorrencias():

    #escopo de autenticação, esse escopo serve para ler e manipular a planilha
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

    #id da planilha e nome da aba + intervalo
    SAMPLE_SPREADSHEET_ID = '1ILU2dxgAkumVD1P3yPt0zN5vZdG8SnWMFYxy47D4biQ'
    SAMPLE_RANGE_NAME = 'ocorrencias!A2:H3000'

    #gerando credenciais
    store = file.Storage('Ocurrences/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('Ocurrences/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    #chamando a planilha do google e consultando seus valores
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values1 = result.get('values', [])



    #values1 recebeu os valores contidos na planilha, cada item da lista (values1) equivale a 1 linha (1 ocorrencia)
    for occurrence in range(len(values1)):
        
        #content será 1 ocorrencia
        content = values1[occurrence]

        #se a linha for maior que 2 (para retirar os titulos da coluna(pode ser ajustado no intervalo da sheet tbm))
        ra = content[2]
        title = content[6]
        text = content[7]

        #cria notificação no tendaEdu com as informações de "content"
        createNotesTendaEdu(ra,title,text)

    #copia as notificações para um histórico (outra planilha)
    writeSpreadSheet(values1)
    
    #deleta os dados da planilha
    deleteSheet()

    return 'ok!'

#essa função cria as notificações no tendaEdu
def createNotesTendaEdu(ra,title,text):

    urlGetInfo_to_Alias = 'https://api.edu.tenda.digital/v1/members/search?alias='+str(ra)


    headers = {

        'community-id': 'vereda-savp',
        'Authorization': 'Bearer '+token_tenda


    }


    response = requests.get(urlGetInfo_to_Alias,headers=headers)


    contenT = json.loads(response.content)


    idStudent = contenT['hits'][0]['_id']


    name = contenT['hits'][0]['name']


    dateExpired = datetime.datetime.now() + datetime.timedelta(days=7)



    #formatando a data na gambiarra kkkk
    year = str(dateExpired.year)


    if len(str(dateExpired.month)) == 1:

        month = '0'+str(dateExpired.month)
    else:

        month = str(dateExpired.month)

    if len(str(dateExpired.day)) == 1:
    
        day = '0'+str(dateExpired.day)
    else:

        day = str(dateExpired.day)


    if len(str(dateExpired.hour)) == 1:
    
        hour = '0'+str(dateExpired.hour)
    else:

        hour = str(dateExpired.hour)


    if len(str(dateExpired.minute)) == 1:
        
        minute = '0'+str(dateExpired.minute)
    else:

        minute = str(dateExpired.minute)


    if len(str(dateExpired.second)) == 1:
        
        second = '0'+str(dateExpired.second)
    else:

        second = str(dateExpired.second)

    
    



    dateExpiredFormat = year+'-'+month+'-'+day+'T'+hour+':'+minute+':'+second+'Z'

    #-------------JSON ENVIADO PARA O TENDAEDU PARA CRIAÇÃO DE NOTIFICAÇÕES------------------------


    url_Message = 'https://api.edu.tenda.digital/v1/post'


    headers2 = {

        'Content-type': 'application/json',
        'community-id': 'vereda-savp',
        'Authorization': 'Bearer '+token_tenda

    }




    labels = {

    "type": "message",
    "title": title,
    "text": text,
        "roles": [
        "guardian"
        ],
        "targets": [
            {
                "_id": idStudent,
                "name": name,
                "type": "member"
            }
    ],
    
    "feedback": {

        "expiresAt": dateExpiredFormat,
        "type": "aware"
    }
    }


    create = requests.post(url_Message,headers=headers2,json=labels)

    #rota que busca notificações de certo usuário
    #url = 'https://api.edu.test.tenda.digital/v1/post?_id=<idUsuario>'



    #-----------------------------------------------------------------------------------------------------------


def writeSpreadSheet(values1):

    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

    SAMPLE_SPREADSHEET_ID = '1ILU2dxgAkumVD1P3yPt0zN5vZdG8SnWMFYxy47D4biQ'
    SAMPLE_RANGE_NAME = 'historico!A2:H3000'


    store = file.Storage('Ocurrences/token2.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('Ocurrences/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))


    sheet = service.spreadsheets()

    # https://developers.google.com/sheets/guides/values#appending_values -- documentação do google para escritas e leituras de sheet
    
    values = {'values':[]}

    for line in values1:
        contentLine = []
        for column in line:
            contentLine.append(column)
        values['values'].append(contentLine)

    result = sheet.values().append(
        spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME,
        valueInputOption='USER_ENTERED',
        body=values).execute()



#OBS: PARA CADA FUNÇÃO QUE CONVERSE COM A API DO GOOGLE, É IMPORTANTE RENOMEAR DENTRO DA FUNÇÃO
#O NOME "token.json", POIS PRECISAMOS DE UM TOKEN DIFERENTE PARA CADA REQUISIÇÃO, 
# as credencias ("credentials.json") podem ser as mesmas para todas as funções.

def deleteSheet():
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

    SAMPLE_SPREADSHEET_ID = '1ILU2dxgAkumVD1P3yPt0zN5vZdG8SnWMFYxy47D4biQ'
    SAMPLE_RANGE_NAME = 'ocorrencias!A2:H3000'


    store = file.Storage('Ocurrences/token3.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('Ocurrences/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))


    sheet = service.spreadsheets()


    request = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()




#DICA: CASO A APLICAÇÃO DÊ PROBLEMAS FUTUROS DE AUTENTICAÇÃO, O PROBLEMA PODERÁ SER OS TOKENS, EXCLUA-OS E TENTE NOVAMENTE
#OU TENTE AS FUNÇÕES SEPARADAMENTE FORA DO PROJETO, OBTENHA OS TOKENS PARA CADA UMA E OS TRAGA PARA DENTRO DO PROJETO.


