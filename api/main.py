from flask import Blueprint
from flask import jsonify
from flask import request
from database.main_data import recetas

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/receta-controler/recetas/', methods=['GET'])
def get_recetas():
    return jsonify(recetas)


@main_blueprint.route('/receta-controler/recetas/<receta_id>', methods=['GET'])
def get_receta(receta_id):
    for r in recetas:
        if r.get('id') == receta_id:
            receta = r
            return jsonify(receta)
    return 'No se encontró la receta'
