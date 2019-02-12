#----------------------------------CRUD DISCIPLINAS----------------------------------------
from app import db
from ModelsDB.tables import Disciplines
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy


#CREATE
def createDisciplines(dados):

    for discipline in dados:

        name = discipline['name']
        description = discipline['description']
        groupYear = discipline['groupYear']


        new = Disciplines(name,description,groupYear)

        new.name = name
        new.description = description
        new.groupYear = groupYear


        db.session.add(new)
        db.session.commit()


#captura todas as disciplinas do ano de ensino informado cadastradas na tabela
#Disciplines
def getDisciplinesGroup(group):


    disciplines = Disciplines.query.filter_by(groupYear=group).all()

    dados = []

    for discipline in disciplines:

        id = discipline._id
        name = discipline.name
        description = discipline.description
        groupYear = discipline.groupYear


        dados.append({'_id':id,'name':name,'description':description,'groupYear':groupYear})



    return dados





