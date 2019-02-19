#--------------------------------------------------CRUD DE FREQUÊNCIAS-------------------------------------------



from app import db
from ModelsDB.tables import daily_frequence, Ausences
from flask_sqlalchemy import SQLAlchemy
from Frequences.functionsFrequence.frequenceDiscipline import getDisciplinesAusences
from Frequences.functionsFrequence.alunos import returnRa
from Frequences.functionsFrequence.crud_periods import select_periods_all
from Frequences.functionsFrequence.crud_disciplines import getDisciplinesGroup


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

#RETORNA FREQUENCIAS DE DETERMINADO ALUNO
def getFrequenceRa(ra):

    aluno = returnRa(ra)

    if aluno != None:

        year = aluno.year

        #retorna frequencias diárias
        dados = getFrequenceDaily_Student(ra)

        #retorna total de frequencias no ano por disciplina
        dadosDisciplina = getDisciplinesAusences(ra,year)


        #retorna frequencias por disciplina e período
        dadosDisciplinaPeriodo = return_frequences_for_periods(ra)


        return {'daily':dados,'disciplines':dadosDisciplina,'disciplines_periods':dadosDisciplinaPeriodo}
    
    else:
        return None


#RETORNA FREQUENCIAS POR PERÍODO PARA UM DETERMINADO ALUNO ESPECIFICANDO A MATÉRIA QUE SE DESEJA OBTER OS DADOS
def return_frequences_for_periods(ra):
    
    #capturamos todos os dados do aluno informado na função
    aluno = returnRa(ra)

    #dentre essas informações capturamos seu ano de ensino
    year = aluno.year

    #guardará dados no formato ex.: {'Matemática':{'1ºTrimestre':4,'2ºTrimestre/1':5,'2ºTrimestre/2':8,'3ºTrimestre':0}}
    #ou seja, a disciplina e as faltas do aluno por período na disciplina
    dic_discipline = {}

    #capturamos todas as disciplinas que o aluno está cadastrado (disciplinas de seu ano de ensino)
    disciplines = getDisciplinesGroup(year)

    #para cada disciplina no ano de ensino do aluno:
    for disciplineDatas in disciplines:

        #pegamos o nome da disciplina
        discipline = disciplineDatas['name']

        #pegamos todos os períodos letivos da escola
        periods = select_periods_all()

        #esse dict guardará os períodos e as faltas dentro de cada período na disciplina em questão
        dic_periods = {}

        #para cada período da escola
        for period in periods:

            #este será o contador de faltas
            cont = 0

            #capturamos o nome do período e quando ele começa e termina (datetime)
            period_name = period['name_periodo']
            init = period['init']
            finish = period['finish']

            #vamos procurar todas as ausencias daquele aluno naquela disciplina
            query_ausences = Ausences.query.filter_by(ra = ra, discipline = discipline).all()


            #para cada ausencia encontrada:
            for ausence in query_ausences:

                #se a ausencia estiver dentro do intervalo de datas em que aquele período existe
                #o contador de faltas receberá +1
                if ausence.date >= init and ausence.date  <= finish:

                    cont = cont+1

            #dicionário dos períodos recebe o nome do período e quantidade de faltas nele pela disciplina em questão
            dic_periods[period_name] = cont

        #o dicionário da disciplina recebe as informações sobre faltas nos períodos e coloca a chave como sendo
        #o nome da disciplina, ou seja, atribui as informações a uma determinada disciplina
        dic_discipline[discipline] = dic_periods

    return dic_discipline


