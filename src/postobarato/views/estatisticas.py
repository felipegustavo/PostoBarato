from flask import Blueprint, render_template

mod_estatisticas = Blueprint('mod_estatisticas', __name__)

@mod_estatisticas.route('/estatisticas')
def estatisticas():
	return render_template('estatisticas.html')