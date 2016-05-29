from flask import Blueprint, render_template, current_app
import json

mod_estatisticas = Blueprint('mod_estatisticas', __name__)

@mod_estatisticas.route('/estatisticas')
def estatisticas():
	with open(current_app.config['BASE_DIR'] + '/database/capitais.json') as arquivo:
		dados = json.load(arquivo)
	return render_template('estatisticas.html', capitais=dados['capitais'])