from flask import Blueprint, render_template

mod_contato = Blueprint('mod_contato', __name__)

@mod_contato.route('/contato')
def contato():
	return render_template('contato.html')