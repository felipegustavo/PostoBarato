from flask import Blueprint, request, render_template, current_app
import json

mod_postos = Blueprint('mod_postos', __name__)

@mod_postos.route('/ver_postos')
def ver_postos():
	acao = request.args.get('acao', '')
	capital_id = request.args.get('capital', '')	
	arquivo_caminho = current_app.config['BASE_DIR'] + '/database/postos/' + capital_id + '.json'

	with open(arquivo_caminho) as arquivo:
		dados = json.load(arquivo)

	if acao == 'mapa':
		return render_template('ver_postos_mapa.html', dados=dados)
	elif acao == 'lista':
		return render_template('ver_postos_lista.html', dados=dados)