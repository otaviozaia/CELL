#-------------------------------------------CHECAGEM E ATRIBUIÇÕES DE FREQUENCIA---------------------------------


from app import db
from ModelsDB.tables import daily_frequence,Grades,Student,Ausences
from flask_sqlalchemy import SQLAlchemy
from Frequences.functionsFrequence.alunos import returnAll,returnRa
from flask import jsonify
import json
from datetime import datetime

#checará a frequencia e inserirá no db
def checkFrequence(datas):

    #data do dia atual
    dateBase = datetime.now()

    #armazenará os dados sobre entrada e saída do aluno e suas informações essenciais para formar presença no dia
    listaDeEventos = createEventList(datas)

    #para cada aluno 
    for row in listaDeEventos:

        #se o aluno esteve ausente no dia (presence?==0)
        #iremos capturar os dados do aluno normalmente, porém vamos atribuir
        #falta para tudo, exceto os períodos nomeados como café ou almoço
        if row['presence?'] == 0:
            ra = row['ra']
            name = row['name']
            weekday = row['events']['weekday']
            date = dateBase
            #retornamos dados do aluno consultando pelo ra que vem da outa função
            #porque precisamos de sua turma para capturar a grade horária correta dele naquele dia
            alunoAtual = returnRa(ra)
            #capturamos a turma pelo atributo group da classe Student
            group = alunoAtual.group

            #obtemos a grade horária do aluno naquela dia buscando por turma e dia da semana
            grade = Grades.query.filter_by(turma=group,diaSemana=weekday).first()

            #se a grade estiver cadastrada
            if grade:
            

                #todos os períodos começam com falta
                p1,p2,p3,p4,p5,p6,p7,p8,p9,p10 = 1,1,1,1,1,1,1,1,1,1

                #se for almoço ou café, o período volta com falta == 0
                if grade.p1materia == 'Almoço' or grade.p1materia == 'Café':

                    p1 = 0

                if grade.p2materia == 'Almoço' or grade.p2materia == 'Café':

                    p2 = 0

                if grade.p3materia == 'Almoço' or grade.p3materia == 'Café':
        
                    p3 = 0

                if grade.p4materia == 'Almoço' or grade.p4materia == 'Café':
        
                    p4 = 0

                if grade.p5materia == 'Almoço' or grade.p5materia == 'Café':
        
                    p5 = 0

                if grade.p6materia == 'Almoço' or grade.p6materia == 'Café':
        
                    p6 = 0

                if grade.p7materia == 'Almoço' or grade.p7materia == 'Café':
        
                    p7 = 0

                if grade.p8materia == 'Almoço' or grade.p8materia == 'Café':
        
                    p8 = 0


                if grade.p9materia == 'Almoço' or grade.p9materia == 'Café':
        
                    p9 = 0

                
                if grade.p10materia == 'Almoço' or grade.p10materia == 'Café':
        
                    p10 = 0

                #entrada e saída são nulos
                entrada = None
                saida = None

                #guardará o número de ausencias
                ausences = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

                total = sum(ausences)

                #criamos um novo objeto do tipo enterExitDatas e o adicionamos na sessão do db 
                #só comitaremos as alterações no final dos loopings
                freq =  daily_frequence(ra,name,date,weekday,entrada,saida,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,total)
            
                freq.ra = ra
                freq.name = name
                freq.date = date
                freq.weekday = weekday
                freq.entrada = entrada
                freq.saida = saida
                freq.p1 = p1
                freq.p2 = p2
                freq.p3 = p3
                freq.p4 = p4
                freq.p5 = p5
                freq.p6 = p6
                freq.p7 = p7
                freq.p8 = p8
                freq.p9 = p9
                freq.p10 = p10
                freq.total = total

                db.session.add(freq)


                #o código abaixo verificará se há faltas nos períodos, se houver, 
                #a falta será registrada na tabela Ausences com ra, matéria e data
                if p1 == 1:
    
                    ra = ra
                    discipline = grade.p1materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)

                if p2 == 1:
    
                    ra = ra
                    discipline = grade.p2materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)

                if p3 == 1:
    
                    ra = ra
                    discipline = grade.p3materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)


                if p4 == 1:
    
                    ra = ra
                    discipline = grade.p4materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)

                
                if p5 == 1:
    
                    ra = ra
                    discipline = grade.p5materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)


                if p6 == 1:
    
                    ra = ra
                    discipline = grade.p6materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)


                if p7 == 1:
    
                    ra = ra
                    discipline = grade.p7materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)


                if p8 == 1:
    
                    ra = ra
                    discipline = grade.p8materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)


                if p9 == 1:
    
                    ra = ra
                    discipline = grade.p9materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)


                if p10 == 1:
    
                    ra = ra
                    discipline = grade.p10materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)


        #se o aluno estiver presente:
        else:
            ra = row['ra']
            name = row['name']
            group = row['group']
            weekday = row['events']['weekday']
            enter = row['events']['ENTRADA'] #capturamos datetime de entrada nos eventos
            exit = row['events']['SAIDA'] #capturamos datetime de saída nos eventos
            date = dateBase


            grade = Grades.query.filter_by(turma=group,diaSemana=weekday).first()

            if grade:

                p1,p2,p3,p4,p5,p6,p7,p8,p9,p10 = 1,1,1,1,1,1,1,1,1,1

                #dividimos date de time para entrada e saída
                crashTimeEnter = enter.split(' ')
                crashTimeExit =  exit.split(' ')

                #capturamos apenas o time
                hourEnter = crashTimeEnter[1]
                hourExit = crashTimeExit[1]

                #separamos os elementos de time
                crashHourEnter = hourEnter.split(':')
                crashHourExit = hourExit.split(':')
                
                #capturamos apenas hora e minutos e transformamos em float
                entrada = float(crashHourEnter[0]+'.'+crashHourEnter[1])
                saida = float(crashHourExit[0]+'.'+crashHourExit[1])


                #comparamos o momento de entrada e saída com cada período (início e fim)
                #para contarmos as presenças
                #cada período possui 15 minutos de tolerancia, ou seja : float(0.15)
                if entrada <= grade.p1init+0.15 and saida >= grade.p1finish:

                    p1 = 0

                if entrada <= grade.p2init+0.15 and saida >= grade.p2finish:

                    p2 = 0

                if entrada <= grade.p3init+0.15 and saida >= grade.p3finish:

                    p3 = 0


                if entrada <= grade.p4init+0.15 and saida >= grade.p4finish:
        
                    p4 = 0


                if entrada <= grade.p5init+0.15 and saida >= grade.p5finish:
        
                    p5 = 0

                
                if entrada <= grade.p6init+0.15 and saida >= grade.p6finish:
        
                    p6 = 0


                if entrada <= grade.p7init+0.15 and saida >= grade.p7finish:
        
                    p7 = 0


                if entrada <= grade.p8init+0.15 and saida >= grade.p8finish:
        
                    p8 = 0


                if entrada <= grade.p9init+0.15 and saida >= grade.p9finish:
        
                    p9 = 0

                
                if entrada <= grade.p10init+0.15 and saida >= grade.p10finish:
        
                    p10 = 0


                if grade.p1materia == 'Almoço' or grade.p1materia == 'Café':
        
                    p1 = 0

                if grade.p2materia == 'Almoço' or grade.p2materia == 'Café':

                    p2 = 0

                if grade.p3materia == 'Almoço' or grade.p3materia == 'Café':
        
                    p3 = 0

                if grade.p4materia == 'Almoço' or grade.p4materia == 'Café':
        
                    p4 = 0

                if grade.p5materia == 'Almoço' or grade.p5materia == 'Café':
        
                    p5 = 0

                if grade.p6materia == 'Almoço' or grade.p6materia == 'Café':
        
                    p6 = 0

                if grade.p7materia == 'Almoço' or grade.p7materia == 'Café':
        
                    p7 = 0

                if grade.p8materia == 'Almoço' or grade.p8materia == 'Café':
        
                    p8 = 0


                if grade.p9materia == 'Almoço' or grade.p9materia == 'Café':
        
                    p9 = 0

                
                if grade.p10materia == 'Almoço' or grade.p10materia == 'Café':
        
                    p10 = 0

                ausences = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

                total = sum(ausences)

                freq =  daily_frequence(ra,name,date,weekday,entrada,saida,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,total)
            
                freq.ra = ra
                freq.name = name
                freq.date = date
                freq.weekday = weekday
                freq.entrada = entrada
                freq.saida = saida
                freq.p1 = p1
                freq.p2 = p2
                freq.p3 = p3
                freq.p4 = p4
                freq.p5 = p5
                freq.p6 = p6
                freq.p7 = p7
                freq.p8 = p8
                freq.p9 = p9
                freq.p10 = p10
                freq.total = total

                db.session.add(freq)

                #o código abaixo verificará se há faltas nos períodos, se houver, 
                #a falta será registrada na tabela Ausences com ra, matéria e data
                if p1 == 1:

                    ra = ra
                    discipline = grade.p1materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)

                if p2 == 1:
    
                    ra = ra
                    discipline = grade.p2materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)

                if p3 == 1:
    
                    ra = ra
                    discipline = grade.p3materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)


                if p4 == 1:
    
                    ra = ra
                    discipline = grade.p4materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)

                
                if p5 == 1:
    
                    ra = ra
                    discipline = grade.p5materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)


                if p6 == 1:
    
                    ra = ra
                    discipline = grade.p6materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)


                if p7 == 1:
    
                    ra = ra
                    discipline = grade.p7materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)


                if p8 == 1:
    
                    ra = ra
                    discipline = grade.p8materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)


                if p9 == 1:
    
                    ra = ra
                    discipline = grade.p9materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)


                if p10 == 1:
    
                    ra = ra
                    discipline = grade.p10materia
                    date = date


                    ausence = Ausences(ra,discipline,date)

                    ausence.ra = ra
                    ausence.discipline = discipline
                    ausence.date = date

                    db.session.add(ausence)


        #comitamos tudo que foi adicionado para o banco
        db.session.commit()


#criará uma lista de eventos por alunos, contendo ra, nome, turma, horário de entrada e saída no seguinte formato:
#[{"events":{"ENTRADA":"2018-10-04 07:01:45","SAIDA":"2018-10-04 15:06:55","weekday":3},"group":"5ºB","name":"CAMILLE GONÇALVES PERES","ra":"3958"}]
def createEventList(datas):

    #guardará somente entrada e saída de cada aluno
    entradaSaida = []

    #retorna todos os alunos
    alunos = returnAll()

    #para cada aluno fazemos uma busca pelo ra dentro do json enviado via post na rota '/frequence/events'
    #capturando sua entrada e saída
    for aluno in alunos:

        #dados trazidos de dentro do db do projeto referentes aos alunos
        ra = aluno['ra']
        name = aluno['name']
        turma = aluno['group']

        #guardará entrada e saída
        events = {}

        #para cada evento vindo do banco de zigLock (que serão entrada ou saída):
        for event in datas:

            #se o evento conter o ra do aluno que o primeiro looping está varrendo no banco do projeto:
            if event['ra'] == ra:

                #captura sua entrada e coloca no "events"
                if event['type'] == 'ENTRADA':
                    events['ENTRADA'] = event['time']

                #ou captura sua saídade e coloca no "events"
                elif event['type'] == 'SAIDA':
                    events['SAIDA'] = event['time']

                #events recebe o numero do dia da semana vindo do json,começando de domingo como 1 até sabado como 7
                events['weekday'] = event['weekday']
        
        #se o events for diferente de vazio, entradaSaida recebe os dados de entrada e saída do aluno +RA + TURMA
        #e presence? == 1
        if events != {}:

            entradaSaida.append({'ra':ra,'name':name,'events':events,'group':turma,'presence?':1})

        #se o events for vazio, ou seja, o aluno não foi encontrado no json vindo da requisição
        #para frequence/events, significa que o aluno faltou
        #ele recebe em seu events: dia da semana e presence? == 0 
        elif events == {}:
            events['weekday'] = datas[0]['weekday']
            entradaSaida.append({'ra':ra,'name':name,'events':events,'group':'','presence?':0})
            

    #return entradaSaida
    return entradaSaida







