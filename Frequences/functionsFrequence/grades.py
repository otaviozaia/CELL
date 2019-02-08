#----------------------------------------CRUD DE GRADES HORÁRIAS--------------------------------------------------



from app import db
from ModelsDB.tables import Grades
from flask_sqlalchemy import SQLAlchemy

#registra grades horárias por turma, dia  da semana
def registerGrades(datas):
    
    #definindo variáveis:
    turma = datas['group']
    diaSemana = datas['weekday']
    p1init = datas['p1']['init']
    p1finish = datas['p1']['finish']
    p1materia = datas['p1']['discipline']
    p2init = datas['p2']['init']
    p2finish = datas['p2']['finish']
    p2materia = datas['p2']['discipline']
    p3init = datas['p3']['init']
    p3finish = datas['p3']['finish']
    p3materia = datas['p3']['discipline']
    p4init = datas['p4']['init']
    p4finish = datas['p4']['finish']
    p4materia = datas['p4']['discipline']
    p5init = datas['p5']['init']
    p5finish = datas['p5']['finish']
    p5materia = datas['p5']['discipline']
    p6init = datas['p6']['init']
    p6finish = datas['p6']['finish']
    p6materia = datas['p6']['discipline']
    p7init = datas['p7']['init']
    p7finish = datas['p7']['finish']
    p7materia = datas['p7']['discipline']
    p8init = datas['p8']['init']
    p8finish = datas['p8']['finish']
    p8materia = datas['p8']['discipline']
    p9init = datas['p9']['init']
    p9finish = datas['p9']['finish']
    p9materia = datas['p9']['discipline']
    p10init = datas['p10']['init']
    p10finish = datas['p10']['finish']
    p10materia = datas['p10']['discipline']




    #criando novo objeto:
    grade = Grades(turma,diaSemana,
                        p1init,p1finish,p1materia,
                        p2init,p2finish,p2materia,
                        p3init,p3finish,p3materia,
                        p4init,p4finish,p4materia,
                        p5init,p5finish,p5materia,
                        p6init,p6finish,p6materia,
                        p7init,p7finish,p7materia,
                        p8init,p8finish,p8materia,
                        p9init,p9finish,p9materia,
                        p10init,p10finish,p10materia)

    grade.turma = turma
    grade.diaSemana = diaSemana
    grade.p1init = p1init
    grade.p1finish = p1finish 
    grade.p1materia = p1materia
    grade.p2init = p2init
    grade.p2finish = p2finish 
    grade.p2materia = p2materia
    grade.p3init = p3init
    grade.p3finish = p3finish 
    grade.p3materia = p3materia
    grade.p4init = p4init
    grade.p4finish = p4finish 
    grade.p4materia = p4materia
    grade.p5init = p5init
    grade.p5finish = p5finish 
    grade.p5materia = p5materia
    grade.p6init = p6init
    grade.p6finish = p6finish 
    grade.p6materia = p6materia
    grade.p7init = p7init
    grade.p7finish = p7finish 
    grade.p7materia = p7materia
    grade.p8init = p8init
    grade.p8finish = p8finish 
    grade.p8materia = p8materia
    grade.p9init = p9init
    grade.p9finish = p9finish 
    grade.p9materia = p9materia
    grade.p10init = p10init
    grade.p10finish = p10finish 
    grade.p10materia = p10materia


    #add no banco de dados
    db.session.add(grade)

    #comitando a operação no banco
    db.session.commit()

def setGrades(datas):

    for row in datas:

        group = row['group']
        weekday = row['weekday']

        grade = Grades.query.filter_by(turma=group,diaSemana=weekday).first()

        grade.turma = row['group']
        grade.diaSemana = row['weekday']
        grade.p1init = row['p1']['init']
        grade.p1finish = row['p1']['finish'] 
        grade.p1materia = row['p1']['discipline']
        grade.p2init = row['p2']['init']
        grade.p2finish = row['p2']['finish']
        grade.p2materia = row['p2']['discipline']
        grade.p3init = row['p3']['init']
        grade.p3finish = row['p3']['finish']
        grade.p3materia = row['p3']['discipline']
        grade.p4init = row['p4']['init']
        grade.p4finish = row['p4']['finish']
        grade.p4materia = row['p4']['discipline']
        grade.p5init = row['p5']['init']
        grade.p5finish = row['p5']['finish']
        grade.p5materia = row['p5']['discipline']
        grade.p6init = row['p6']['init']
        grade.p6finish = row['p6']['finish']
        grade.p6materia = row['p6']['discipline']
        grade.p7init = row['p7']['init']
        grade.p7finish = row['p7']['finish']
        grade.p7materia = row['p7']['discipline']
        grade.p8init = row['p8']['init']
        grade.p8finish = row['p8']['finish']
        grade.p8materia = row['p8']['discipline']
        grade.p9init =row['p9']['init']
        grade.p9finish = row['p9']['finish']
        grade.p9materia = row['p9']['discipline']
        grade.p10init = row['p10']['init']
        grade.p10finish = row['p10']['finish']
        grade.p10materia = row['p10']['discipline']

        db.session.commit()


def getGradesAll():

    grades = Grades.query.all()


    dados = []


    for grade in grades:

        dados.append({'id':grade._id,
                        'turma':grade.turma,
                        'diaSemana':grade.diaSemana,
                        'p1init':grade.p1init,
                        'p1finish':grade.p1finish,
                        'p1materia':grade.p1materia,
                        'p2init':grade.p2init,
                        'p2finish':grade.p2finish,
                        'p2materia':grade.p2materia,
                        'p3init':grade.p3init,
                        'p3finish':grade.p3finish,
                        'p3materia':grade.p3materia,
                        'p4init':grade.p4init,
                        'p4finish':grade.p4finish,
                        'p4materia':grade.p4materia,
                        'p5init':grade.p5init,
                        'p5finish':grade.p5finish,
                        'p5materia':grade.p5materia,
                        'p6init':grade.p6init,
                        'p6finish':grade.p6finish,
                        'p6materia':grade.p6materia,
                        'p7init':grade.p7init,
                        'p7finish':grade.p7finish,
                        'p7materia':grade.p7materia,
                        'p8init':grade.p8init,
                        'p8finish':grade.p8finish,
                        'p8materia':grade.p8materia,
                        'p9init':grade.p9init,
                        'p9finish':grade.p9finish,
                        'p9materia':grade.p9materia,
                        'p10init':grade.p10init,
                        'p10finish':grade.p10finish,
                        'p10materia':grade.p10materia})

    return dados
