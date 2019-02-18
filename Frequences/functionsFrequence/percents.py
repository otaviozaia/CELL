#-----------------------------MÓDULO RESPONSÁVEL POR CALCULAR PORCENTAGENS DE FREQUENCIAS-------------------------
from Frequences.functionsFrequence.return_frequence import return_frequences_for_periods
from Frequences.functionsFrequence.alunos import returnRa
from ModelsDB.tables import QuantidadeAulas

#retornará as porcentagens de frequencia por matéria e período:
def return_percent_for_discipline(ra):

    result = {}


    #retorna as disciplinas do aluno, seus periodos e totais de falta
    disciplines_and_total_periods_ausences = return_frequences_for_periods(ra)

    #retorna o aluno para podermos capturar seu ano de ensino
    aluno = returnRa(ra)

    #ano de ensino do aluno
    year = aluno.year

    #para cada disciplina e períodos (estes sendo períodos e total de falta por cada um):
    for discipline, periods in disciplines_and_total_periods_ausences.items():
        
        dict_discipline_periods = {}

        #para cada período e total de faltas:
        for period, totals in periods.items():

            query_classes = QuantidadeAulas.query.filter_by(discipline_name=discipline,discipline_year=year,discipline_period=period).first()

            if query_classes != None:

                total_ausences = totals

                total_classes = query_classes.qnt_classes

                percent_frequence = round((total_classes-total_ausences)/(total_classes/100),2)

                percent_ausence = round(100 - percent_frequence,2)

                percent_f = str(percent_frequence)+'%'

                percent_a = str(percent_ausence)+'%'

                dict_discipline_periods[period] = {'Porcentagem Frequência':percent_f,'Porcentagem Ausência':percent_a}

        result[discipline] = dict_discipline_periods


    return result
