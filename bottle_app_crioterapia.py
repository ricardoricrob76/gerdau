#Autor: Ricardo Roberto de Lima - 2018 -> projeto de bottle
#Conjunto de importacoes
from bottle import default_app, template, request, post, get
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib

#Definição das possíveis rotas para a função de callback
#Domínio da Crioterapia com Verrugas

@get('/')
@get('/form/')
def index():
     #Definição de valores iniciais para as expressões animal, classificação e probabilidade
     return template('/home/ricardorobertolima/mysite/formulario-crioterapia.html', nome = "-", classificacao = "-", probabilidade = "-")

#Definição da rota e função de callback
@post('/form/')
def index_resposta():
    #Pega os valores informados no formulário e atribui a variaveis locais
    nome = request.forms.get('nome')
    sexo = request.forms.get('sexo')
    idade = request.forms.get('idade')
    tempo = request.forms.get('tempo')
    nverrugas = request.forms.get('nverrugas')
    tipo = request.forms.get('tipo')
    area = request.forms.get('area')

    modelo_NB = GaussianNB()
    #Carrega o modelo gerado
    modelo_NB = joblib.load('/home/ricardorobertolima/mysite/modelo_crioterapia_MNB.pkl')
    #Executa a classificação
    res = modelo_NB.predict([[int(sexo), int(idade), int(tempo), int(nverrugas), int(tipo), int(area)]])

    #Encontra o valor da confidência
    probabilidade = modelo_NB.predict_proba([[int(sexo), int(idade), int(tempo), int(nverrugas), int(tipo), int(area)]])

    if res == 1:
        classificacao = "Resultado do Tratamento foi: Positivo"
    elif res == 0:
        classificacao = "Resultado do Tratamento foi: Negativo"
    else:
        classificacao = "Indefinido"

    #Renderiza o template com os valores passados como argumento
    return template('/home/ricardorobertolima/mysite/formulario-crioterapia.html', nome = animal, classificacao = classificacao, probabilidade = probabilidade)
    #return template('/home/ricardorobertolima/mysite/Formulario.html', animal = animal, classificacao = classificacao)

application = default_app()
