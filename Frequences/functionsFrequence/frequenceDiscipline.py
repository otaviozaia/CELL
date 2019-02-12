#-------------------------ARQUIVO QUE GUARDARÁ FALTAS POR MATÉRIAS-------------------------------------
from app import db
from ModelsDB.tables import Disciplines, Ausences
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from Frequences.functionsFrequence.crud_disciplines import getDisciplinesGroup


#função que filtrará as disciplinas pela turma do aluno e coletará as faltas por matéria
def getDisciplinesAusences(ra,group):

    #lista que guardará matérias/disciplinas como chaves e faltas como valores (ausencesToDiscipline)
    dictAusencesToDisciplines = []


    #retorna todas as disciplinas da turma do aluno (group)
    disciplines = getDisciplinesGroup(group)

    #para cada disciplina da turma do aluno retornamos as faltas que ele tem em cada uma
    for discipline in disciplines:

        #lista que guardará todas as ausencias do aluno em determinada disciplina
        ausencesToDiscipline = []


        #então coletamos o nome da disciplina
        nameDiscipline = discipline['name']

        #e fazemos a consulta no bd de faltas por ra e disciplina (para trimestres filtraremos por date tbm)
        ausencesDiscipline = Ausences.query.filter_by(ra=ra,discipline=nameDiscipline).all()

        #se houver ausencias
        if ausencesDiscipline != None:

            #para cada ausencia encontrada:
            for ausences in ausencesDiscipline:

                #capturamos a data da ausencia e adicionamos ela em uma lista 
                date = ausences.date

                ausencesToDiscipline.append(date)

        #o dicionário recebe matéria e quantidade de faltas         
        dictAusencesToDisciplines.append({nameDiscipline:len(ausencesToDiscipline)})

    #retorna json de matérias vs faltas 
    return dictAusencesToDisciplines







