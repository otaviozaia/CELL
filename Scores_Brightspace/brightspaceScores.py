#-------------------CAPTURA NOTAS DE ALUNOS NO BRIGHTSPACE LMS E AS MOSTRA NO TENDAEDU----------------------------



from flask import jsonify, request, render_template, redirect
import json
import requests
import d2lvalence.auth as d2lauth #importando módulos de autenticação do brightspace
from app import app




#com o processo de autenticação descrito na documentação da api >> https://docs.valence.desire2learn.com/clients/python/index.html (Tópico Usage), conseguimos a URL redirect_url para fazermos o restante do processo
def requestApi(ra):

    #guardará nomes e ids dos curso ativos do aluno
    courseId_Name_Avals = {}
    
    #essas são chaves que nos são dadas quando registramos nossa api no nosso domínio do brightspace
    app_creds = { 'app_id': 'D8teWNVT6hq1H1SnLuMgrw', 'app_key': 'Q-kcTUvf6J4Q5LNWVxFmLQ' }

    #criando contexto de aplicação
    ac = d2lauth.fashion_app_context(app_id=app_creds['app_id'], app_key=app_creds['app_key'])

    #url base para criar contexto de usuário, conseguimos essa url seguindo os passos de autenticação descritos na documentação da api d2l (Brightspace): https://docs.valence.desire2learn.com/clients/python/index.html TÓPICO "Usage"

    #url para o domínio teste (demo)
    #redirect_url = 'https://vereda-notas.herokuapp.com/test-api?x_a=_387hhfpi7ffMBIUp52kEV&x_b=gy__zGuRE5q9ZPpRsNTdk8&x_c=zTzmPE_7IFhObhuIlerBYbRPwG5e8_a-bTUb2mpsJek'

    redirect_url = 'https://vereda-notas.herokuapp.com/test-api?x_a=Gcndek5_edg05alriWkiW5&x_b=g9Apf8heMFSBd5P1xp-Stb&x_c=EtlJk8IuLX1p6rBaYpADTzQEeHEH1qi1CtZchfrRZOQ'
                

    #criando contexto de usuário
    uc = ac.create_user_context(result_uri=redirect_url, host='escolavereda.brightspace.com', encrypt_requests=True)


    #-----------------------------------EXEMPLO DE ROTAS------------------------------------------------------------

    #ID DO ALUNO EM QUESTÃO: 226

    #rota por aluno no curso de inglês(6695)(notas objetos): '/d2l/api/le/1.0/6695/grades/values/226/' 3º PASSO

    #rota por aluno no curso de inglês(6695)(nota final calculada): '/d2l/api/le/(version)/(orgUnitId)/grades/final/values/(userId)' 4º PASSO

    #rota pra todos os users : '/d2l/api/lp/1.0/users/'

    #cursos do aluno : '/d2l/api/lp/1.0/enrollments/users/226/orgUnits/' 2º PASSO

    #pesquisar aluno por RA: '/d2l/api/lp/1.0/users/?OrgDefinedId=1701998' 1º PASSO

    #-----------------------------------REQUISIÇÃO PARA OBTER ID NO SISTEMA, DO ALUNO--------------------------------

    #informamos a rota que captura informações sobre todos os usuários
    route1 = '/d2l/api/lp/1.0/users/' 

    #autenticamos a rota
    url1 = uc.create_authenticated_url(route1)
   
    #fazemos a requisição concatenando parâmetros para enviar via GET, o parâmetro busca um usuário específico pelo "ID Definido pela Instituição" no Brightspace
    #"ID Definido pela instituição" deve ser o mesmo "ALIAS" retornado do tendaEdu
    r1 = requests.get(url1+'&OrgDefinedId='+ra)

    if r1.status_code == 404:

        message = 'Aluno não cadastrado em Vereda Digital.'

        dic = {'Erro: ':message}

        return dic

    else:
        #recebe informações sobre usuário, dentre elas o id definido pelo SISTEMA BRIGHTSPACE
        dadosStudent = json.loads(r1.content)

        #capturamos o id de sistema do usuário para as futuras requisições
        id = dadosStudent[0]['UserId']

        #-----------------------------------REQUSIÇÃO PARA OBTER INFORMAÇÕES SOBRE CURSOS DO ALUNO----------------------

        route2 = '/d2l/api/lp/1.0/enrollments/users/'+str(id)+'/orgUnits/'


        url2 = uc.create_authenticated_url(route2)


        r2 =  requests.get(url2)

        #coletará json que contem informações gerais sobre os cursos do aluno dentre outros dados
        orgUnits = json.loads(r2.content)

        #pegará no json apenas as informações sobre cursos que estará dentro de 'Items'
        courses = orgUnits['Items']

        #Items é uma lista
        for course in courses:
            #exemplo de estrutura para course: ----------------------------------------------------------------------------
            #{
            #	"OrgUnit": {
            #		"Id": 6695,
            #		"Type": {
            #			"Id": 3,
            #			"Code": "Course Offering",
            #			"Name": "Oferta de Curso"
            #		},
            #		"Name": "Língua Inglesa - 2º Ano",
            #		"Code": "VLIEF02"
            #	},
            #	"Role": {
            #		"Id": 103,
            #		"Code": "",
            #		"Name": "Student"
            #	}
            #}
            #----------------------Acrescentando nome e id de curso no dicionário courseId_Name----------------------------
            if course['OrgUnit']['Type']['Code'] != 'Organization' and course['OrgUnit']['Type']['Code'] != 'Group':
                
                #nome do curso
                nameCourse = course['OrgUnit']['Name']
                
                #id do curso
                idCourse = str(course['OrgUnit']['Id'])#convertemos para string porque iremos utilizar em requisições


                courseId_Name_Avals[idCourse] = {nameCourse:{}}

            #RESULTADO exemplo: {'6695': {'Língua Inglesa - 2º Ano': {}}, '6698': {'Ciências - 8º Ano ': {}}}


            #-------------------------------ADICIONANDO NOME DOS OBJETOS E NOTAS-------------------------------------------

            #se o aluno estiver matriculado em alguma disciplina:
            if courseId_Name_Avals != {}:

                #key será o id do curso e o value será o nome
                for key,value in courseId_Name_Avals.items():

                    #rota que pegará informações sobre os objetos(avaliações) do curso utilizando id (curso) e id(aluno)
                    route3 = '/d2l/api/le/1.0/'+key+'/grades/values/'+str(id)+'/'


                    url3 = uc.create_authenticated_url(route3)

                    
                    r3 =  requests.get(url3)


                    if r3.status_code <= 200:

                        datasObjects = json.loads(r3.content)


                        #os passos seguintes só irão acontecer se dataObjects existir, senão irá para o próximo looping (próximo curso)
                        #k será o nome do curso em courseId_Name_Avals e v será um dic vazio, os dois sempre terão tamanho len(0)
                        for k,v in value.items():

                            #objects serão as avaliações
                            for objects in datasObjects:

                                #nome da avaliação
                                nameAval =  objects['GradeObjectName']

                                #nota da avaliação
                                scoreAval = objects['DisplayedGrade']

                                #v é o nosso dicionário vazio dentro do nome do curso, recebe nome como chave e nota como valor 
                                v[nameAval] = scoreAval

                                #RESULTADO exemplo:["{'6695': {'Língua Inglesa - 2º Ano': {'Aval teste inglês ': '66,67%', 'Nota trimestral': '100%'}}, '6698': {'Ciências - 8º Ano ': {}}}]"


                #--------------------------------------CAPTURANDO NOTA FINAL DE CADA CURSO------------------------------------

                            route4 = '/d2l/api/le/1.0/'+key+'/grades/final/values/'+str(id)

                            url4 = uc.create_authenticated_url(route4)

                            r4 =  requests.get(url4)

                            #se o curso tiver uma nota final já computada (só não terá se não houverem avaliações, porém se for vazio dará erro) :
                            if r4.status_code <= 200:

                                dadosFinalscore = json.loads(r4.content)


                                v['Nota Final'] = dadosFinalscore['DisplayedGrade']
            
                            else:
                                v['Nota Final'] = 'Indefinida'

                #-------------------------------------------------------------------------------------------------------------                            

            #se o aluno não estiver cadastrado em alguma disciplina:
            elif courseId_Name_Avals == {}:

                message = 'Aluno não cadastrado em disciplinas!'

                courseId_Name_Avals['Erro: '] = message


        return courseId_Name_Avals  






#essa rota será usada apenas como rota de confiança para formarmos a url final de requisição para o brightspace
@app.route("/test-api")
def testApi():

    return None




#no ambiente tenda será colocada uma rota de requisição para nossa API com o token de sessão do usuário e seu community-id
#/push-key?token=TOKEN&community=COMMUNITY
@app.route("/push-key",methods=['GET'])#rota que será colocada no tenda para requisição na nossa api, o que está entre "<>" são variáveis
def getDados():

    token = request.args.get("token")
    community = request.args.get("community")
    #armazenará resposta final
    datas = None
    #armazenará os alias e nomes existentes no json inserido em 'datas'
    raS = []
    names = []
    #armazenará os cursos(disciplinas) e médias por aluno
    studentScores = []



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
        dataScores = requestApi(ra)
        studentScores.append(dataScores)

    return render_template('index.html',names=names,raS=raS,studentScores=studentScores)