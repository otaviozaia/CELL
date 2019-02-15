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
#importa funções CRUD para disciplinas
from Frequences.functionsFrequence.crud_disciplines import*
#importa funções de frequencia
from Frequences.functionsFrequence.frequenceDiscipline import*
#importa funções crud de períodos(trimestres)
from Frequences.functionsFrequence.crud_periods import*
#importa funções crud de quantidade de aulas por matéria
from Frequences.functionsFrequence.crud_qnt_classes import*





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

    return 'successfull!'


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

    return 'successfull!'

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

    return 'successfull!'


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


#retorna frequencias diárias e por matérias/disciplinas
#frequence?token=TOKEN&community=COMMUNITY
@app.route('/frequence')
def getFrequenceByStudent():

    token = request.args.get("token")
    community = request.args.get("community")
    #armazenará resposta final
    datas = None
    #armazenará os alias e nomes existentes no json inserido em 'datas'
    raS = []
    names = []
    frequencesStudy = []


    api_url_base = 'https://api.edu.tenda.digital/v1' #rota padrão para todas as requisições feitas à API do tenda
    #os headers são recebidos na rota pelas variáveis token e community
    headers1 = {'community-id':community,
               'Content-type':'application/json',
               'Authorization':'Bearer {0}'.format(token)}
    
    #definindo rota de requisição para a API do tenda. */use/me? é utilizada para recuperar todas as informações sobre um usuário
    api_url = '{0}/user/me?'.format(api_url_base)

    #a variável response guardará o retorno da requisição feita ao tenda
    response = requests.get(api_url,headers=headers1)

    # variável datas recebe resultado do response em json
    datas = json.loads(response.content)

    #escolhemos os itens que queremos retornar dentro do json, aqui no caso o alias (identificador (no menu contas) e ID (ID quando for registrar aluno no menu alunos)) * obs: alias seria o RA
    #alias =  datas['members'][0]['alias']

    #armazeno na variável array todos os alias de alunos associados à conta 'familiar' 
    if raS == []:
        for i in range(len(datas['members'])):
            raS.append(datas['members'][i]['alias'])

    if names == []:
        for name in range(len(datas['members'])):
            names.append(datas['members'][name]['name'])

    for ra in raS:

        frequences = getFrequenceRa(ra)

        if frequences != None:
            frequencesStudy.append(frequences)

    #exemplo json frequencesStudy:
    #[
    # { 'daily':
    #   [{"_id":1,
    #   "date":"13/2/2019",
    #   "entrada":8.01,
    #   "name":"FILHO 1",
    #   "p1":1,"p10":1,
    #   "p2":0,
    #   "p3":0,
    #   "p4":0,
    #   "p5":0,
    #   "p6":0,
    #   "p7":0,
    #   "p8":0,
    #   "p9":0,
    #   "ra":"1701998",
    #   "saida":15.06,
    #   "total":2,
    #   "weekday":"Segunda-feira"}
    #   ],
    #   'disciplines':
    #   [
    #   {"TEP":1},
    #   {"Geografia":0},
    #   {"Língua Portuguesa":0},
    #   {"Língua Inglesa":0},
    #   {"Educação Física":1},
    #   {"TEP Duplo Fixo":0},
    #   {"Matemática":0},{"Ciências":0},
    #   {"História":0}
    #   ]
    # },
    # 
    # { 'daily':
    #  [{"_id":2,
    #   "date":"13/2/2019",
    #   "entrada":9.01,
    #   "name":"FILHO 2",
    #   "p1":1,
    #   "p10":1,
    #   "p2":1,
    #   "p3":0,
    #   "p4":0,
    #   "p5":0,
    #   "p6":0,
    #   "p7":0,
    #   "p8":0,
    #   "p9":1,
    #   "ra":"1701999",
    #   "saida":14.06,
    #   "total":4,
    #   "weekday":
    #   "Segunda-feira"}
    #   ],
    #   'disciplines':
    #   [
    #   {"TEP":2},
    #   {"Geografia":0},
    #   {"Língua Portuguesa":0},
    #   {"Língua Inglesa":0},
    #   {"Educação Física":2},
    #   {"TEP Duplo Fixo":0},
    #   {"Matemática":0},
    #   {"Ciências":0},
    #   {"História":0}
    #   ]
    #  }
    #]


    #return jsonify(frequencesStudy)

    return render_template('frequence.html',frequencesStudy=frequencesStudy)



#-------------------------------------------------DISCIPLINAS----------------------------------------------------



#rota para criação de disciplinas
@app.route('/disciplines/create',methods=['POST'])
def disciplineCreate():

    dados = request.get_json()


    #json sample:
    '''
    [

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

    ]
    '''

    createDisciplines(dados)


    return 'successfull'



#-------------------------------------------PERÍODOS(TRIMESTRES)-------------------------------------------------



@app.route('/periods/insert',methods=['POST'])
def insertPeriods():

    datas = request.get_json()

    #json sample:

    '''
    json = [
      {'name':'1ºTrimestre','inicio':'28-1-2019','final':'31-3-2019'},
      {'name':'2ºTrimestre/1','inicio':'1-4-2019','final':'20-6-2019'},
      {'name':'Férias','inicio':'21-6-2019','final':'31-7-2019'},
      {'name':'2ºTrimestre/2','inicio':'1-8-2019','final':'10-9-2019'},
      {'name':'3ºTrimestre','inicio':'1-10-2019','final':'30-9-2019'}
    ]
    '''


    insert_periods(datas)


    return 'Successfull'



#--------------------------------------------------TOTAIS AULAS POR PERÍODOS-------------------------------------

'''
@app.route('periods/classes-insert',methods=['POST'])
def insertQntClasess():

    datas = request.get_json()

    #json sample
  



  

    insert_qnt_classes(datas)

    return 'successfull' 
'''