# app/routes.py
import random
import socket
from flask import Blueprint, jsonify, render_template
from .models import pokeneas

bp = Blueprint('main', __name__)

def get_container_id():
    return socket.gethostname()

@bp.route('/api/pokenea', methods=['GET'])
def api_pokenea():
    p = random.choice(pokeneas)
    result = {
        "id": p["id"],
        "nombre": p["nombre"],
        "altura": p["altura"],
        "habilidad": p["habilidad"],
        "contenedor_id": get_container_id()
    }
    return jsonify(result), 200

@bp.route('/show/pokenea', methods=['GET'])
def show_pokenea():
    p = random.choice(pokeneas)
    return render_template('pokenea.html', pokenea=p, contenedor_id=get_container_id())
