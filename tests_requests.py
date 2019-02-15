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
'''


def test_check_frequences(client):
    
    labels = [

        {"type":"ENTRADA",
        "time":"2018-10-04 07:01:45",
        "name":"FILHO 1",
        "ra":"1701998",
        "weekday":3},

        {"type":"ENTRADA",
        "time":"2018-10-04 12:45:45",
        "name":"FILHO 1",
        "ra":"1701998",
        "weekday":3},

        {"type":"ENTRADA",
        "time":"2018-10-04 13:30:45",
        "name":"FILHO 1",
        "ra":"1701998",
        "weekday":3},
        
        {"type":"SAIDA",
        "time":"2018-10-04 15:22:55",
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

