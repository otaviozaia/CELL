from app import db
from ModelsDB.tables import Periodos
from datetime import datetime


#--------------------------------------------CRUD DE PERIODOS-------------------------------------------------


#cadastra períodos no banco de dados:
def insert_periods(datas):
    
    #para cada periodo recebido no json capturamos o nome, data de inicio e data de fim
    for period in datas:

        name_periodo = period['name']
        dateInit = period['inicio'].split('-')#transformamos a data em uma lista para conseguirmos converter em datetime 
        dateFinish = period['final'].split('-')

        init = datetime(int(dateInit[2]),int(dateInit[1]),int(dateInit[0]))#init recebe a lista gerada com os dados da data convertidas em datetime
        finish = datetime(int(dateFinish[2]),int(dateFinish[1]),int(dateFinish[0]))#finish a mesma coisa citada acima

        #criamos o novo objeto do tipo periodo e o adicionamos ao banco
        period = Periodos(name_periodo,init,finish)

        period.name_periodo = name_periodo
        period.init = init
        period.finish = finish


        db.session.add(period)

    #salvamos as modificações e fechamos a conexão
    db.session.commit()      

