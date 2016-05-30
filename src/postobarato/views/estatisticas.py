from flask import Blueprint, request, render_template, current_app
import json, os

mod_estatisticas = Blueprint('mod_estatisticas', __name__)

@mod_estatisticas.route('/estatisticas')
def estatisticas():
	with open(current_app.config['BASE_DIR'] + '/database/estatisticas.json') as arquivo:
		dados = json.load(arquivo)

	local_id = request.args.get('local', '')	
	if local_id:
		arquivo_caminho = current_app.config['BASE_DIR'] + '/database/estatisticas/' + local_id + '.json'
		if os.path.isfile(arquivo_caminho):
			with open(arquivo_caminho) as arquivo:
				statistics = json.load(arquivo)
			return render_template('estatisticas.html', capitais=dados['estatisticas'], statistics=statistics)
		else:
			arquivo_caminho = current_app.config['BASE_DIR'] + '/database/estatisticas/brasil.json'
			with open(arquivo_caminho) as arquivo:
				statistics = json.load(arquivo)
			return render_template('estatisticas.html', capitais=dados['estatisticas'], statistics=statistics)
	else:
		arquivo_caminho = current_app.config['BASE_DIR'] + '/database/estatisticas/brasil.json'
		with open(arquivo_caminho) as arquivo:
			statistics = json.load(arquivo)

		return render_template('estatisticas.html', capitais=dados['estatisticas'], statistics=statistics)