from flask import Flask, request, redirect, url_for, \
	render_template
import json

# configurations
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
	return redirect('busca_postos')

@app.route('/busca_postos')
def busca_postos():
	with open('database/capitais.json') as arquivo:
		dados = json.load(arquivo)
	return render_template('busca_postos.html', capitais=dados['capitais'])

@app.route('/contato')
def contato():
	return render_template('contato.html')

@app.route('/sobre')
def sobre():
	return render_template('sobre.html')

@app.route('/ver_postos')
def ver_postos():
	acao = request.args.get('acao', '')
	capital_id = request.args.get('capital', '')	
	arquivo_caminho = 'database/postos/' + capital_id + '.json'

	with open(arquivo_caminho) as arquivo:
		dados = json.load(arquivo)

	if acao == 'mapa':
		return render_template('ver_postos_mapa.html', dados=dados)
	elif acao == 'lista':
		return render_template('ver_postos_lista.html', dados=dados)


if __name__ == '__main__':
	app.run()