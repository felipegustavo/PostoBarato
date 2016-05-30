from flask import Blueprint, redirect, render_template, current_app, request

mod_rota = Blueprint('mod_rota', __name__)

@mod_rota.route('/rota')
def rota():
	nome = request.args.get('nome', '')
	lat = request.args.get('lat', '')
	lng = request.args.get('lng', '')
	return render_template('rota.html', nome=nome, lat=lat, lng=lng)