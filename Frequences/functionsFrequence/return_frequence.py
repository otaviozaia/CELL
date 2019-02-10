#--------------------------------------------------CRUD DE FREQUÊNCIAS-------------------------------------------



from app import db
from ModelsDB.tables import daily_frequence
from flask_sqlalchemy import SQLAlchemy



#RETORNA FREQUENCIAS DE UM DETERMINADO ALUNO BUSCANDO PELO RA
def getFrequenceDaily_Student(ra):

    #armazenará lista com frequencias diárias de um aluno
    dados = []

    #trazendo todas as frequencias de um determinado aluno
    frequence = daily_frequence.query.filter_by(ra=ra).all()

    for daily in frequence:

        #formatando data
        timeDate = daily.date

        dia = timeDate.day
        mes = timeDate.month
        ano = timeDate.year

        formatDate = str(dia)+'/'+str(mes)+'/'+str(ano)

        #nomeando dia da semana
        if daily.weekday == 2:
            weekDay = 'Segunda-feira'
        elif daily.weekday == 3:
            weekDay = 'Terça-feira'
        elif daily.weekday == 4:
            weekDay = 'Quarta-feira'
        elif daily.weekday == 5:
            weekDay = 'Quinta-feira'
        elif daily.weekday == 6:
            weekDay = 'Sexta-feira'
        elif daily.weekday == 7:
            weekDay = 'Sábado'
        elif daily.weekday == 1:
            weekDay = 'Domingo'

        #formando json a ser retornado pela função
        dados.append({'_id':daily._id,
                        'ra':daily.ra,
                        'name':daily.name,
                        'date':formatDate,
                        'weekday':weekDay,
                        'entrada':daily.entrada,
                        'saida':daily.saida,
                        'p1':int(daily.p1),
                        'p2':int(daily.p2),
                        'p3':int(daily.p3),
                        'p4':int(daily.p4),
                        'p5':int(daily.p5),
                        'p6':int(daily.p6),
                        'p7':int(daily.p7),
                        'p8':int(daily.p8),
                        'p9':int(daily.p9),
                        'p10':int(daily.p10),
                        'total':daily.total})

    return dados





    
