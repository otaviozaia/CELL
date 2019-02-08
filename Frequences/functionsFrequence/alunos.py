#----------------------------------------RESPONSÁVEL POR CRUD DOS ALUNOS----------------------------------------

from app import db
from ModelsDB.tables import Student
from flask_sqlalchemy import SQLAlchemy


#insere alunos a partir de um dado json enviado
def registerDatas(datas):

    for row in datas['datas']:

        _ra = row[0]
        name = row[1]
        group = row[2]
        year = row[3]


        student = Student(_ra,name,group,year)
        student._ra = _ra
        student.name = name
        student.group = group
        student.year = year

        db.session.add(student)
        db.session.commit()




#deleta alunos a partir de um dado json enviado
def deleteDatas(identifier):

    aluno = Student.query.filter_by(ra=identifier).first()

    if not aluno:
        return False
    db.session.delete(aluno)
    db.session.commit()
    return True    



#retorna todos os alunos
def returnAll():

    alunos =  Student.query.all()
    
    dados = []

    for aluno in alunos:
        dados.append({'id':aluno._pk,'ra':aluno.ra,'name':aluno.name,'group':aluno.group,'year':aluno.year})

    return dados

#função que retorna aluno por ra
def returnRa(ra):

    aluno = Student.query.filter_by(ra=ra).first()

    return aluno
