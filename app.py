#----------------------------------------------SERVER E CONFIGURAÇÕES DO APP-------------------------------------
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from credenciais import*

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ra.db"
app.config['SQLALCHEMY_DATABASE_URI'] = string_bd_connection_mysql
app.config['JSON_AS_ASCII'] = False #para UTF-8
db = SQLAlchemy(app)

#importa os componentes e as rotas do módulo de visualização de notas do brightspace para o tendaEdu
from Scores_Brightspace.brightspaceScores import*
#importa funções e rotas do módulo de ocorrencias
from Ocurrences.quickstart import*
#importa rotas utilizadas para troca de dados no que se diz respeito a frequências,
#alunos e grades horárias.
from Frequences.frequence import*

#roda servidor local
if __name__ == '__main__':
    app.run(debug=False)




