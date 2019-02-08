#--------------------------------ROTAS PARA FREQUENCIAS, ALUNOS E GRADES HORÁRIAS-----------------------------------

from app import app
from app import db
from flask import jsonify, request, render_template, redirect
import json
import requests
from ModelsDB.tables import Student
#importa as funções criadas para CRUD de alunos
from Frequences.functionsFrequence.alunos import* 
#importa as funções referentes ao CRUD de grade horária
from Frequences.functionsFrequence.grades import*
#importa funções da checagem de presenças
from Frequences.functionsFrequence.check_frequence import*
#importa funções que retornam presenças dos alunos
from Frequences.functionsFrequence.return_frequence import*


#------------------------------------------------ALUNOS-------------------------------------------------------------

#rota para inserir alunos 
@app.route("/students/insert",methods=['POST'])
def insertStudent():

    #json sample:

    #json = {'datas':[

    #    [ra,name,group,year],
    #    [ra,name,group,year],
    #    [ra,name,group,year]

    #]}


    #executa função registerDatas com o dado enviado via POST
    registerDatas(request.get_json())


@app.route("/students/delete",methods=["POST"])
def deleteStudent():

    #json sample:

    #json = {'datas':[

    #    ra,
    #    ra,
    #    ra

    #]}

    #captura o json enviado pela requisição
    datas = request.get_json()

    #pra cada dado (ra) no valor da chave 'datas' dentro da variável datas(que é um dicionário), deleta um aluno
    for row in datas['datas']:

        ra = row

        deleteDatas(ra)

#ROTA PARA RETORNAR ALUNOS
#/students?option=all
#or
#/students?option=one&ra=1701999
@app.route('/students',methods=['GET'])
def getStudents():

    option = request.args.get("option")

    if option == 'all':

        return jsonify(returnAll())

    elif option == 'one':

        ra = request.args.get("ra")

        aluno = returnRa(ra)

        dados = {'id':aluno._pk,'ra':aluno.ra,'name':aluno.name,'group':aluno.group,'year':aluno.year}

        return jsonify(dados)




#-----------------------------------------------GRADES HORÁRIAS----------------------------------------------------


#cadastro de grade-horária
@app.route('/frequence/insert-grids',methods=['POST'])
def insertGrades():

    datas = request.get_json()

    #json sample:


    '''
    json = [{'group':'5ºB',
    'weekday':2,
    'p1':{'init':7,'finish':7.50,'discipline':'Matemática'},
    'p2':{'init':7.50,'finish':8.40,'discipline':'História'},
    'p3':{'init':8.40,'finish':9,'discipline':'Café'},
    'p4':{'init':9,'finish':9.50,'discipline':'Geografia'},
    'p5':{'init':9.50,'finish':10.40,'discipline':'Geografia'},
    'p6':{'init':10.40,'finish':11.30,'discipline':'Matemática'},
    'p7':{'init':11.30,'finish':12.30,'discipline':'Almoço'},
    'p8':{'init':12.30,'finish':13.20,'discipline':'Português'},
    'p9':{'init':13.20,'finish':14.10,'discipline':'Português'},
    'p10':{'init':14.10,'finish':15,'discipline':'Ciências'}
    
    },
    {'group':'5ºB',
    'weekday':3,
    'p1':{'init':7,'finish':7.50,'discipline':'Física'},
    'p2':{'init':7.50,'finish':8.40,'discipline':'História'},
    'p3':{'init':8.40,'finish':9,'discipline':'Café'},
    'p4':{'init':9,'finish':9.50,'discipline':'Matemática'},
    'p5':{'init':9.50,'finish':10.40,'discipline':'Matemática'},
    'p6':{'init':10.40,'finish':11.30,'discipline':'Português'},
    'p7':{'init':11.30,'finish':12.30,'discipline':'Almoço'},
    'p8':{'init':12.30,'finish':13.20,'discipline':'Português'},
    'p9':{'init':13.20,'finish':14.10,'discipline':'Ciências'},
    'p10':{'init':14.10,'finish':15,'discipline':'Ciências'}
    
    }
    
    ]

    '''

    for grade in datas:

        registerGrades(grade)




@app.route('/frequence/set-grids',methods=['POST'])
def setGrids():

    datas = request.get_json()

    #json sample:


    '''
    json = [{'group':'5ºB',
    'weekday':2,
    'p1':{'init':7,'finish':7.50,'discipline':'Matemática'},
    'p2':{'init':7.50,'finish':8.40,'discipline':'História'},
    'p3':{'init':8.40,'finish':9,'discipline':'Café'},
    'p4':{'init':9,'finish':9.50,'discipline':'Geografia'},
    'p5':{'init':9.50,'finish':10.40,'discipline':'Geografia'},
    'p6':{'init':10.40,'finish':11.30,'discipline':'Matemática'},
    'p7':{'init':11.30,'finish':12.30,'discipline':'Almoço'},
    'p8':{'init':12.30,'finish':13.20,'discipline':'Português'},
    'p9':{'init':13.20,'finish':14.10,'discipline':'Português'},
    'p10':{'init':14.10,'finish':15,'discipline':'Ciências'}
    
    },
    {'group':'5ºB',
    'weekday':3,
    'p1':{'init':7,'finish':7.50,'discipline':'Física'},
    'p2':{'init':7.50,'finish':8.40,'discipline':'História'},
    'p3':{'init':8.40,'finish':9,'discipline':'Café'},
    'p4':{'init':9,'finish':9.50,'discipline':'Matemática'},
    'p5':{'init':9.50,'finish':10.40,'discipline':'Matemática'},
    'p6':{'init':10.40,'finish':11.30,'discipline':'Português'},
    'p7':{'init':11.30,'finish':12.30,'discipline':'Almoço'},
    'p8':{'init':12.30,'finish':13.20,'discipline':'Português'},
    'p9':{'init':13.20,'finish':14.10,'discipline':'Ciências'},
    'p10':{'init':14.10,'finish':15,'discipline':'Ciências'}
    
    }
    
    ]

    '''

    setGrades(datas)

#rota para retornar todas as grades horárias
@app.route('/frequence/get-grids',methods=['GET'])
def getGrids():

    dados = getGradesAll()

    return jsonify(dados)





    

#---------------------------------------------------FREQUÊNCIAS---------------------------------------------------



#essa rota será responsável por receber dados (POST) referentes a entrada e saída dos alunos, checar 
# suas faltas e fazer suas 
#frequências diárias
@app.route('/frequence/events',methods=['POST'])
def frequenceCheck():

    #input json sample:

    '''
    json = [

        {"type":"ENTRADA",
        "time":"2018-10-04 07:01:45",
        "name":"CAMILLE GONÇALVES PERES",
        "ra":"3958",
        "weekday":3},
        
        {"type":"SAIDA",
        "time":"2018-10-04 15:06:55",
        "name":"CAMILLE GONÇALVES PERES",
        "ra":"3958",
        "weekday":3}

    ]

    '''
    datas = request.get_json()

    checkFrequence(datas)


    return 'successfull!'

#RETORNA FREQUENCIAS DE DETERMINADO ALUNO
#/frequence/return?ra=3958
@app.route('/frequence/return')
def getFrequenceRa():

    ra = request.args.get("ra")

    dados = getFrequenceDaily_Student(ra)

    return jsonify(dados)




