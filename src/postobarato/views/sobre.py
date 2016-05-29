from flask import Blueprint, render_template

mod_sobre = Blueprint('mod_sobre', __name__)

@mod_sobre.route('/sobre')
def sobre():
	return render_template('sobre.html')