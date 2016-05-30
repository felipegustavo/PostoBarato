# -*- coding: utf-8 -*-
from flask import Flask

# App
app = Flask(__name__, instance_relative_config=True)

# Config
app.config.from_object('postobarato.config')

# Blueprints
from postobarato.views.busca import mod_busca
app.register_blueprint(mod_busca)

from postobarato.views.contato import mod_contato
app.register_blueprint(mod_contato)

from postobarato.views.sobre import mod_sobre
app.register_blueprint(mod_sobre)

from postobarato.views.postos import mod_postos
app.register_blueprint(mod_postos)

from postobarato.views.estatisticas import mod_estatisticas
app.register_blueprint(mod_estatisticas)

from postobarato.views.rota import mod_rota
app.register_blueprint(mod_rota)