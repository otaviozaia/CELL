#---------------------------------------FILE PARA TESTES AUTOMATIZADOS----------------------------------------------------

import os
import tempfile

import pytest


from app import app

#---------------------------------------CONFIG BASE PARA TESTES (CLIENTE)---------------------------------------
@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
 
    yield client


#------------------------------------------TESTANDO ROTAS:-------------------------------------------------------------
'''
#TESTANDO ROTA DE OCORRENCIAS
def test_ocurrences(client):

    res = client.get('/ocurrences')
    assert res.status_code == 200  or res.status_code == 404


#TESTANDO ROTA QUE RETORNA NOTAS DOS FILHOS DE UM USUÁRIO DO TENDAEDU
#Scores_Brightspace.brightspaceScores
def test_push_key(client):
    
    res = client.get('/push-key?token=<TOKEN USUARIO>&community=vereda-savp')   
    assert res.status_code == 200


#TESTANDO ROTA QUE RETORNA FREQUENCIA DOS FILHOS DE UM RESPONSÁVEL DO TENDAEDU  
#Frequences.frequence  
def test_return_frequence(client):

    res = client.get('/frequence?token=<TOKEN USUARIO>&community=vereda-savp')
    assert res.status_code == 200



def test_check_frequences(client):
    
    labels = [

        {"type":"ENTRADA",
        "time":"2018-10-04 08:01:45",
        "name":"FILHO 1",
        "ra":"1701998",
        "weekday":3},
        
        {"type":"SAIDA",
        "time":"2018-10-04 14:22:55",
        "name":"FILHO 1",
        "ra":"1701998",
        "weekday":3},

        {"type":"ENTRADA",
        "time":"2018-10-04 09:01:45",
        "name":"FILHO 2",
        "ra":"1701999",
        "weekday":3},

        {"type":"ENTRADA",
        "time":"2018-10-04 12:41:45",
        "name":"FILHO 2",
        "ra":"1701999",
        "weekday":3},

        {"type":"ENTRADA",
        "time":"2018-10-04 13:39:45",
        "name":"FILHO 2",
        "ra":"1701999",
        "weekday":3},
        
        {"type":"SAIDA",
        "time":"2018-10-04 15:22:55",
        "name":"FILHO 2",
        "ra":"1701999",
        "weekday":3}

    ]

    res = client.post('/frequence/events',json=labels)
    assert res.status_code == 200



def test_insert_grid(client):

    json = [{'group':'1ºA',
    'weekday':4,
    'p1':{'init':7.35,'finish':8.1,'discipline':'Matemática'},
    'p2':{'init':8.25,'finish':9,'discipline':'História'},
    'p3':{'init':9.15,'finish':9.5,'discipline':'TEP'},
    'p4':{'init':9.5,'finish':10.01,'discipline':'Café'},
    'p5':{'init':10.25,'finish':11,'discipline':'Geografia'},
    'p6':{'init':11.15,'finish':11.5,'discipline':'Matemática'},
    'p7':{'init':12.05,'finish':12.4,'discipline':'Almoço'},
    'p8':{'init':12.4,'finish':13.40,'discipline':'Almoço'},
    'p9':{'init':13.55,'finish':14.3,'discipline':'Português'},
    'p10':{'init':14.45,'finish':15.2,'discipline':'Ciências'}
    
    },
    {'group':'1ºA',
    'weekday':5,
    'p1':{'init':7.35,'finish':8.1,'discipline':'Matemática'},
    'p2':{'init':8.25,'finish':9,'discipline':'História'},
    'p3':{'init':9.15,'finish':9.5,'discipline':'TEP'},
    'p4':{'init':9.5,'finish':10.01,'discipline':'Café'},
    'p5':{'init':10.25,'finish':11,'discipline':'Geografia'},
    'p6':{'init':11.15,'finish':11.5,'discipline':'Matemática'},
    'p7':{'init':12.05,'finish':12.4,'discipline':'Almoço'},
    'p8':{'init':12.4,'finish':13.40,'discipline':'Almoço'},
    'p9':{'init':13.55,'finish':14.3,'discipline':'Português'},
    'p10':{'init':14.45,'finish':15.2,'discipline':'Ciências'}
    
    },
    {'group':'1ºA',
    'weekday':6,
    'p1':{'init':7.35,'finish':8.1,'discipline':'Matemática'},
    'p2':{'init':8.25,'finish':9,'discipline':'História'},
    'p3':{'init':9.15,'finish':9.5,'discipline':'TEP'},
    'p4':{'init':9.5,'finish':10.01,'discipline':'Café'},
    'p5':{'init':10.25,'finish':11,'discipline':'Geografia'},
    'p6':{'init':11.15,'finish':11.5,'discipline':'Matemática'},
    'p7':{'init':12.05,'finish':12.4,'discipline':'Almoço'},
    'p8':{'init':12.4,'finish':13.40,'discipline':'Almoço'},
    'p9':{'init':13.55,'finish':14.3,'discipline':'Português'},
    'p10':{'init':14.45,'finish':15.2,'discipline':'Ciências'}
    
    },
    
    ]

    res = client.post('/frequence/insert-grids',json=json)
    assert res.status_code == 200


def test_insertStudents(client):

    #inserir alunos aqui

    res = client.post('/students/insert',json=json)
    assert res.status_code == 200


def test_create_disciplines(client):

    json = [

        {'name':'TEP',
        'description':'TESTE',
         'groupYear':1},
         {'name':'Geografia',
        'description':'TESTE',
         'groupYear':1},
         {'name':'Língua Portuguesa',
        'description':'TESTE',
         'groupYear':1},
         {'name':'Língua Inglesa',
        'description':'TESTE',
         'groupYear':1},
         {'name':'Educação Física',
        'description':'TESTE',
         'groupYear':1}, 
         {'name':'TEP Duplo Fixo',
        'description':'TESTE',
         'groupYear':1},
         {'name':'Matemática',
        'description':'TESTE',
         'groupYear':1},
         {'name':'Ciências',
        'description':'TESTE',
         'groupYear':1},
         {'name':'História',
        'description':'TESTE',
         'groupYear':1},

    ]

    res = client.post('/disciplines/create',json=json)
    assert res.status_code == 200




#testando crud de periodos:
def test_insert_periods(client):

    labels = [
      {'name':'1ºTrimestre','inicio':'28-1-2019','final':'31-3-2019'},
      {'name':'2ºTrimestre/1','inicio':'1-4-2019','final':'20-6-2019'},
      {'name':'Férias','inicio':'21-6-2019','final':'31-7-2019'},
      {'name':'2ºTrimestre/2','inicio':'1-8-2019','final':'10-9-2019'},
      {'name':'3ºTrimestre','inicio':'1-10-2019','final':'30-9-2019'}
    ]


    res = client.post('/periods/insert',json=labels)
    assert res.status_code == 200

'''



