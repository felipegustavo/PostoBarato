from flask import Blueprint, redirect, render_template, current_app
import json

mod_busca = Blueprint('mod_busca', __name__)

@mod_busca.route('/')
def index():
	return redirect('busca_postos')

@mod_busca.route('/busca_postos')
def busca_postos():
	with open(current_app.config['BASE_DIR'] + '/database/capitais.json') as arquivo:
		dados = json.load(arquivo)
	return render_template('busca_postos.html', capitais=dados['capitais'])