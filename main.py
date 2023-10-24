from flask import Flask, render_template,url_for,request, redirect
import requests
from forms import Form_rodada
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.environ.get("API_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = '29cecf8afd6176f06bb3f55472d490d1'

@app.route("/")
def inicio():
    return render_template('inicio.html')


@app.route("/brasil")
def C_brasil():
    brasil = 'BSA'

    url = f'http://api.football-data.org/v4/competitions/{brasil}/standings'
    headers = api_key

    response = requests.get(url, headers=headers)
    brasil = response.json()
    #ano = brasil['filters']['season']
    lista = brasil['standings'][0]
    lista_posicao = lista['table']

    return render_template('tabela.html', lista_posicao=lista_posicao)


@app.route("/espanha")
def C_espanha():
    espanha = 'PD'
    url = f'http://api.football-data.org/v4/competitions/{espanha}/standings'
    headers = api_key

    response = requests.get(url, headers=headers)
    brasil = response.json()
    ano = brasil['filters']['season']
    lista = brasil['standings'][0]
    lista_posicao = lista['table']

    return render_template('c_espanha.html', lista_posicao=lista_posicao)


@app.route("/portugal")
def C_portugal():
    portugal = 'PPL'
    url = f'http://api.football-data.org/v4/competitions/{portugal}/standings'
    headers = api_key

    response = requests.get(url, headers=headers)
    brasil = response.json()
    ano = brasil['filters']['season']
    lista = brasil['standings'][0]
    lista_posicao = lista['table']

    return render_template('c_portugal.html', lista_posicao=lista_posicao)


@app.route("/italia")
def C_italia():
    italia = 'SA'
    url = f'http://api.football-data.org/v4/competitions/{italia}/standings'
    headers = api_key

    response = requests.get(url, headers=headers)
    italia = response.json()
    lista = italia['standings'][0]
    lista_posicao = lista['table']
    return render_template('c_italia.html', lista_posicao=lista_posicao)


@app.route("/alemanha")
def C_alemanha():
    alemanha = 'BL1'
    url = f'http://api.football-data.org/v4/competitions/{alemanha}/standings'
    headers = api_key

    response = requests.get(url, headers=headers)
    italia = response.json()
    lista = italia['standings'][0]
    lista_posicao = lista['table']
    return render_template('c_alemanha.html', lista_posicao=lista_posicao)


@app.route("/holanda")
def C_holanda():
    holanda = 'DED'
    url = f'http://api.football-data.org/v4/competitions/{holanda}/standings'
    headers = api_key

    response = requests.get(url, headers=headers)
    italia = response.json()
    lista = italia['standings'][0]
    lista_posicao = lista['table']
    return render_template('c_holanda.html', lista_posicao=lista_posicao)


@app.route("/ingles")
def C_ingles():
    ingles = 'PL'
    url = f'http://api.football-data.org/v4/competitions/{ingles}/standings'
    headers = api_key

    response = requests.get(url, headers=headers)
    italia = response.json()
    lista = italia['standings'][0]
    lista_posicao = lista['table']
    return render_template('c_ingles.html', lista_posicao=lista_posicao)


@app.route("/franca")
def C_franca():
    franca = 'FL1'
    url = f'http://api.football-data.org/v4/competitions/{franca}/standings'
    headers = api_key

    response = requests.get(url, headers=headers)
    italia = response.json()
    lista = italia['standings'][0]
    lista_posicao = lista['table']
    return render_template('c_franca.html', lista_posicao=lista_posicao)


@app.route("/brasil/partidas",methods=['GET', 'POST'])
def p_brasil():
    form_rodada = Form_rodada()

    brasil = 'BSA'
    rodada = form_rodada.rodada.data
    url = f'http://api.football-data.org/v4/competitions/{brasil}/standings'
    headers = api_key
    user = request.form.get('RODADA')
    response = requests.get(url, headers=headers)
    italia = response.json()
    lista = italia['standings'][0]
    lista_posicao = lista['table']

    if form_rodada.validate_on_submit():
        jogos = form_rodada.rodada.data
    else:
        for i in lista_posicao:
            jogos = i['playedGames']

    headers = {'X-Auth-Token': '1f4173cba77f44a9b0cafd42e483f4ea'}
    urs = f'https://api.football-data.org/v4/competitions/{brasil}/matches?matchday={jogos}'
    response = requests.get(urs, headers=headers)
    brasil = response.json()
    lista = brasil['matches']

    return render_template('p_brasil.html',form_rodada=form_rodada, lista=lista,jogos=jogos, rodada=rodada)


@app.route("/espanha/partidas", methods=['GET', 'POST'])
def p_espanha():
    form_rodada = Form_rodada()

    espanha = 'PD'
    rodada = form_rodada.rodada.data
    url = f'http://api.football-data.org/v4/competitions/{espanha}/standings'
    headers = api_key
    user = request.form.get('RODADA')
    response = requests.get(url, headers=headers)
    italia = response.json()
    lista = italia['standings'][0]
    lista_posicao = lista['table']

    if form_rodada.validate_on_submit():
        jogos = form_rodada.rodada.data
    else:
        for i in lista_posicao:
            jogos = i['playedGames']

    headers = {'X-Auth-Token': '1f4173cba77f44a9b0cafd42e483f4ea'}
    urs = f'https://api.football-data.org/v4/competitions/{espanha}/matches?matchday={jogos}'
    response = requests.get(urs, headers=headers)
    brasil = response.json()
    lista = brasil['matches']

    return render_template('p_espanha.html', form_rodada=form_rodada, lista=lista, jogos=jogos, rodada=rodada)


@app.route("/portugal/partidas", methods=['GET', 'POST'])
def p_portugal():
    form_rodada = Form_rodada()
    portugal = 'PPL'
    rodada = form_rodada.rodada.data
    url = f'http://api.football-data.org/v4/competitions/{portugal}/standings'
    headers = api_key
    user = request.form.get('RODADA')
    response = requests.get(url, headers=headers)
    italia = response.json()
    lista = italia['standings'][0]
    lista_posicao = lista['table']

    if form_rodada.validate_on_submit():
        jogos = form_rodada.rodada.data
    else:
        for i in lista_posicao:
            jogos = i['playedGames']

    headers = {'X-Auth-Token': '1f4173cba77f44a9b0cafd42e483f4ea'}
    urs = f'https://api.football-data.org/v4/competitions/{portugal}/matches?matchday={jogos}'
    response = requests.get(urs, headers=headers)
    brasil = response.json()
    lista = brasil['matches']

    return render_template('p_portugal.html', form_rodada=form_rodada, lista=lista, jogos=jogos, rodada=rodada)


@app.route("/italia/partidas", methods=['GET', 'POST'])
def p_italia():
    form_rodada = Form_rodada()
    italia = 'SA'
    rodada = form_rodada.rodada.data
    url = f'http://api.football-data.org/v4/competitions/{italia}/standings'
    headers = api_key
    user = request.form.get('RODADA')
    response = requests.get(url, headers=headers)
    italia1 = response.json()
    lista = italia1['standings'][0]
    lista_posicao = lista['table']
    lista_jogos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if form_rodada.validate_on_submit():
        jogos = form_rodada.rodada.data
    else:
        for i in lista_posicao:
            jogos = i['playedGames']

    headers = {'X-Auth-Token': '1f4173cba77f44a9b0cafd42e483f4ea'}
    urs = f'https://api.football-data.org/v4/competitions/{italia}/matches?matchday={jogos}'
    response = requests.get(urs, headers=headers)
    brasil = response.json()
    lista = brasil['matches']

    return render_template('p_italia.html', form_rodada=form_rodada, lista=lista, jogos=jogos, rodada=rodada)


@app.route("/alemanha/partidas", methods=['GET', 'POST'])
def p_alemanha():
    form_rodada = Form_rodada()
    alemanha = 'BL1'
    rodada = form_rodada.rodada.data
    url = f'http://api.football-data.org/v4/competitions/{alemanha}/standings'
    headers = api_key
    user = request.form.get('RODADA')
    response = requests.get(url, headers=headers)
    alemanha1 = response.json()
    lista = alemanha1['standings'][0]
    lista_posicao = lista['table']
    lista_jogos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if form_rodada.validate_on_submit():
        jogos = form_rodada.rodada.data
    else:
        for i in lista_posicao:
            jogos = i['playedGames']

    headers = {'X-Auth-Token': '1f4173cba77f44a9b0cafd42e483f4ea'}
    urs = f'https://api.football-data.org/v4/competitions/{alemanha}/matches?matchday={jogos}'
    response = requests.get(urs, headers=headers)
    brasil = response.json()
    lista = brasil['matches']

    return render_template('p_alemanha.html', form_rodada=form_rodada, lista=lista, jogos=jogos, rodada=rodada)


@app.route("/holanda/partidas", methods=['GET', 'POST'])
def p_holanda():
    form_rodada = Form_rodada()
    holanda = 'DED'
    rodada = form_rodada.rodada.data
    url = f'http://api.football-data.org/v4/competitions/{holanda}/standings'
    headers = api_key
    user = request.form.get('RODADA')
    response = requests.get(url, headers=headers)
    holanda1 = response.json()
    lista = holanda1['standings'][0]
    lista_posicao = lista['table']
    vali = lista_posicao['position']

    if form_rodada.validate_on_submit():
        jogos = int(form_rodada.rodada.data)
    else:
        for i in lista_posicao:
            jogos = int(i['playedGames'])

    headers = {'X-Auth-Token': '1f4173cba77f44a9b0cafd42e483f4ea'}
    urs = f'https://api.football-data.org/v4/competitions/{holanda}/matches?matchday={jogos}'
    response = requests.get(urs, headers=headers)
    brasil = response.json()
    lista = brasil['matches']

    return render_template('p_holanda.html', form_rodada=form_rodada, lista=lista, jogos=jogos, rodada=rodada)


@app.route("/ingles/partidas", methods=['GET', 'POST'])
def p_ingles():
    form_rodada = Form_rodada()
    ingles = 'PL'
    rodada = form_rodada.rodada.data
    url = f'http://api.football-data.org/v4/competitions/{ingles}/standings'
    headers = api_key
    user = request.form.get('RODADA')
    response = requests.get(url, headers=headers)
    ingles1 = response.json()
    lista = ingles1['standings'][0]
    lista_posicao = lista['table']

    if form_rodada.validate_on_submit():
        jogos = form_rodada.rodada.data
    else:
        for i in lista_posicao:
            jogos = i['playedGames']

    headers = {'X-Auth-Token': '1f4173cba77f44a9b0cafd42e483f4ea'}
    urs = f'https://api.football-data.org/v4/competitions/{ingles}/matches?matchday={jogos}'
    response = requests.get(urs, headers=headers)
    brasil = response.json()
    lista = brasil['matches']

    return render_template('p_ingles.html', form_rodada=form_rodada, lista=lista, jogos=jogos, rodada=rodada)


@app.route("/franca/partidas", methods=['GET', 'POST'])
def p_franca():
    form_rodada = Form_rodada()
    franca = 'FL1'
    rodada = form_rodada.rodada.data
    url = f'http://api.football-data.org/v4/competitions/{franca}/standings'
    headers = api_key
    user = request.form.get('RODADA')
    response = requests.get(url, headers=headers)
    franca1 = response.json()
    lista = franca1['standings'][0]
    lista_posicao = lista['table']
    lista_jogos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if form_rodada.validate_on_submit():
        jogos = form_rodada.rodada.data

    else:
        for i in lista_posicao:
            jogos = i['playedGames']

    headers = {'X-Auth-Token': '1f4173cba77f44a9b0cafd42e483f4ea'}
    urs = f'https://api.football-data.org/v4/competitions/{franca}/matches?matchday={jogos}'
    response = requests.get(urs, headers=headers)
    brasil = response.json()
    lista = brasil['matches']

    return render_template('p_franca.html', form_rodada=form_rodada, lista=lista, jogos=jogos, rodada=rodada)

@app.route("/autor")
def autor():
    return render_template('autor.html')

if __name__ == '__main__':
    app.run(debug=True)
