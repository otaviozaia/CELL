#--------------------------------------------------CRUD DE FREQUÊNCIAS-------------------------------------------



from app import db
from ModelsDB.tables import daily_frequence
from flask_sqlalchemy import SQLAlchemy



#RETORNA FREQUENCIAS DE UM DETERMINADO ALUNO BUSCANDO PELO RA
def getFrequenceDaily_Student(ra):

    dados = []

    frequence = daily_frequence.query.filter_by(ra=ra).all()

    for day in frequence:

        dados.append({'_id':day._id,
                        'ra':day.ra,
                        'name':day.name,
                        'date':day.date,
                        'weekday':day.weekday,
                        'entrada':day.entrada,
                        'saida':day.saida,
                        'p1':day.p1,
                        'p2':day.p2,
                        'p3':day.p3,
                        'p4':day.p4,
                        'p5':day.p5,
                        'p6':day.p6,
                        'p7':day.p7,
                        'p8':day.p8,
                        'p9':day.p9,
                        'p10':day.p10,
                        'total':day.total})

    return dados





    