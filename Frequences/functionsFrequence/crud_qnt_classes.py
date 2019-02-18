from app import db
from ModelsDB.tables import QuantidadeAulas, Periodos, Ausences


#------------------------------------------------CRUD DE QUANTIDADE DE AULAS POR MATÉRIA--------------------------



def insert_qnt_classes(datas):

    for discipline in datas:
        discipline_name = discipline['name']
        discipline_year = discipline['year']
        discipline_period = discipline['period']
        qnt_classes = discipline['qnt']

        discipline_qnt = QuantidadeAulas(discipline_name,discipline_year,discipline_period,qnt_classes)

        discipline_qnt.discipline_name = discipline_name
        discipline_qnt.discipline_year = discipline_year
        discipline_qnt.discipline_period = discipline_period
        discipline_qnt.qnt_classes = qnt_classes

        db.session.add(discipline_qnt)


    db.session.commit()




