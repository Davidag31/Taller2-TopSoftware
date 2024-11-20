from flask import Blueprint, jsonify, render_template, redirect, url_for
from .pokeneas import POKENEAS
import random
import os
import socket

main_bp = Blueprint('main', __name__)

def get_container_id():
    try:
        # Intentar obtener el nombre del host usando socket
        return socket.gethostname()
    except AttributeError:
        return os.uname()[1]

def generate_pokenea_data(pokenea):
    """Genera el diccionario con la información del pokenea."""
    return {
        'id': pokenea['id'],
        'nombre': pokenea['nombre'],
        'altura': pokenea['altura'],
        'habilidad': pokenea['habilidad'],
        'container_id': get_container_id(),
        'frase_filosofica': pokenea['frase_filosofica'],
    }

@main_bp.route('/')
def index_redirect():
    return redirect(url_for('main.display_pokenea'))

@main_bp.route('/json')
def get_pokenea_json():
    pokenea = random.choice(POKENEAS)
    return jsonify(generate_pokenea_data(pokenea))

@main_bp.route('/index')
def display_pokenea():
    pokenea = random.choice(POKENEAS)
    return render_template('index.html', pokenea=pokenea, container_id=get_container_id())
