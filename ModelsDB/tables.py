#----------------------------------CLASSES ORM (TABLES DATABASE)------------------------------------------------


from app import db

#criação de tabelas:


#1 - crie as classes

#2 - acesse a raiz do projeto pelo CMD ou Shell e abra o shell do python digitando "python" no console: 
#python
#Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
#Type "copyright", "credits" or "license()" for more information.
#>>> 

#3 - no shell do python importe as configurações do banco:
#Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
#Type "copyright", "credits" or "license()" for more information.
#>>> from app import db


#4 - entre no diretório ModelsDB no caso do nosso projeto e importe a classe (table) que deseja criar do arquivo tables.py
#>>>from ModelsDB.tables import Test


#5 - de o comando de criação
#>>>db.create_all()


#6 - salve as modificações
#>>>db.session.commit()



#Base de alunos com ra, nome, turma e ano de ensino
class Student(db.Model):
    __tablename__='Student'

    _pk = db.Column(db.Integer, primary_key = True, autoincrement= True)
    ra = db.Column(db.String(20))
    name = db.Column(db.String(100))
    group = db.Column(db.String(40))
    year = db.Column(db.Integer)

    
    def __init__(self,ra,name,group,year):
        self.ra = ra
        self.name = name
        self.group = group
        self.year = year

    def getRa(self):

        return self.ra


    def getName(self):

        return self.name

    def getGroup(self):

        return self.group




#coleta a grade horária por turma e dia da semana contando 10 períodos
class Grades(db.Model):
    __tablename__='Grades'
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    turma = db.Column(db.String(200))
    diaSemana =  db.Column(db.Integer)
    p1init = db.Column(db.Float(precision='4,2'))
    p1finish = db.Column(db.Float(precision='4,2'))
    p1materia = db.Column(db.String(100))
    p2init = db.Column(db.Float(precision='4,2'))
    p2finish = db.Column(db.Float(precision='4,2'))
    p2materia = db.Column(db.String(100))
    p3init = db.Column(db.Float(precision='4,2'))
    p3finish = db.Column(db.Float(precision='4,2'))
    p3materia = db.Column(db.String(100))
    p4init = db.Column(db.Float(precision='4,2'))
    p4finish = db.Column(db.Float(precision='4,2'))
    p4materia = db.Column(db.String(100))
    p5init = db.Column(db.Float(precision='4,2'))
    p5finish = db.Column(db.Float(precision='4,2'))
    p5materia = db.Column(db.String(100))
    p6init = db.Column(db.Float(precision='4,2'))
    p6finish = db.Column(db.Float(precision='4,2'))
    p6materia = db.Column(db.String(100))
    p7init = db.Column(db.Float(precision='4,2'))
    p7finish = db.Column(db.Float(precision='4,2'))
    p7materia = db.Column(db.String(100))
    p8init = db.Column(db.Float(precision='4,2'))
    p8finish = db.Column(db.Float(precision='4,2'))
    p8materia = db.Column(db.String(100))
    p9init = db.Column(db.Float(precision='4,2'))
    p9finish = db.Column(db.Float(precision='4,2'))
    p9materia = db.Column(db.String(100))
    p10init = db.Column(db.Float(precision='4,2'))
    p10finish = db.Column(db.Float(precision='4,2'))
    p10materia = db.Column(db.String(100))

    def __init__(self,
                turma,diaSemana,
                p1init,p1finish,p1materia,
                p2init,p2finish,p2materia,
                p3init,p3finish,p3materia,
                p4init,p4finish,p4materia,
                p5init,p5finish,p5materia,
                p6init,p6finish,p6materia,
                p7init,p7finish,p7materia,
                p8init,p8finish,p8materia,
                p9init,p9finish,p9materia,
                p10init,p10finish,p10materia):

        
        self.turma = turma
        self.diaSemana = diaSemana
        self.p1init = p1init
        self.p1finish = p1finish
        self.p1materia = p1materia
        self.p2init = p2init
        self.p2finish = p2finish
        self.p2materia = p2materia
        self.p3init = p3init
        self.p3finish = p3finish
        self.p3materia = p3materia
        self.p4init = p4init
        self.p4finish = p4finish
        self.p4materia = p4materia
        self.p5init = p5init
        self.p5finish = p5finish
        self.p5materia = p5materia
        self.p6init = p6init
        self.p6finish = p6finish
        self.p6materia = p6materia
        self.p7init = p7init
        self.p7finish = p7finish
        self.p7materia = p7materia
        self.p8init = p8init
        self.p8finish = p8finish
        self.p8materia = p8materia
        self.p9init = p9init
        self.p9finish = p9finish
        self.p9materia = p9materia
        self.p10init = p10init
        self.p10finish = p10finish
        self.p10materia = p10materia


   

#os dados fonte para criação dessa tabela, serão recebidos via POST pela rota '/frequence/events' em frequence.py
#p1, p2 etc significam faltas nos períodos, sendo 0 para nenhuma falta, 1 para falta.      
class daily_frequence(db.Model):
    __tablename__='daily_frequence'
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    ra = db.Column(db.String(20))
    name = db.Column(db.String(100))
    date = db.Column(db.Date)
    weekday = db.Column(db.Integer)
    entrada = db.Column(db.Float(precision='4,2'))
    saida = db.Column(db.Float(precision='4,2'))
    p1 = db.Column(db.Boolean,default=0)
    p2 = db.Column(db.Boolean,default=0)
    p3 = db.Column(db.Boolean,default=0)
    p4 = db.Column(db.Boolean,default=0)
    p5 = db.Column(db.Boolean,default=0)
    p6 = db.Column(db.Boolean,default=0)
    p7 = db.Column(db.Boolean,default=0)
    p8 = db.Column(db.Boolean,default=0)
    p9 = db.Column(db.Boolean,default=0)
    p10 = db.Column(db.Boolean,default=0)
    total = db.Column(db.Integer)


    def __init__(self,
                ra,
                name,
                date,
                weekday,
                entrada,
                saida,
                p1,
                p2,
                p3,
                p4,
                p5,
                p6,
                p7,
                p8,
                p9,
                p10,
                total):
        
        self.ra = ra
        self.name = name
        self.date = date
        self.weekday = weekday
        self.entrada = entrada
        self.saida = saida
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.p7 = p7
        self.p8 = p8
        self.p9 = p9
        self.p10 = p10
        self.total = total



#repositório geral, guardará faltas de alunos contendo ra, disciplina da falta e data (data para posteriormente
# filtrarmos por períodos (trimestre, ano letivo e etc))
class Ausences(db.Model):
    __tablename__='Ausences'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ra = db.Column(db.String(20))
    discipline = db.Column(db.String(100))
    date = db.Column(db.Date)

    def __init__(self, ra, discipline, date):
        self.ra = ra
        self.discipline = discipline
        self.date = date



#disciplinas cadastradas por ano
class Disciplines(db.Model):
    __tablename__='Disciplines'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    groupYear = db.Column(db.Integer)

    def __init__(self, name, description, groupYear):
        self.name = name
        self.description = description
        self.groupYear = groupYear


#guardará os períodos e suas datas de inicio e fim (1º Trimestre, 2ºTrimestre...)
class Periodos(db.Model):
    __tablename__='periodos'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_periodo = db.Column(db.String(40))
    init = db.Column(db.Date)
    finish = db.Column(db.Date)


    def __init__(self, name_periodo, init, finish):
        self.name_periodo = name_periodo
        self.init = init
        self.finish = finish

#guardará a quantidade de aulas por disciplina e períodos (1º Trimestre, 2º Trimestre e ano todo)
class QuantidadeAulas(db.Model):
    __tablename__='quantidade_aulas'
    _id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    discipline_name = db.Column(db.String(100))
    discipline_year = db.Column(db.Integer)
    discipline_period = db.Column(db.String(40))
    qnt_classes = db.Column(db.Integer)

    def __init__(self, discipline_name, discipline_period, discipline_year, qnt_classes):
        self.discipline_name = discipline_name
        self.discipline_period = discipline_period
        self.discipline_year = discipline_year
        self.qnt_classes = qnt_classes





























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































