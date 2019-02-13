#---------------------------------------TESTES AUTOMATIZADOS----------------------------------------------------

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

    res = client.get('frequence?token=<TOKEN USUARIO>&community=vereda-savp')
    assert res.status_code == 200


