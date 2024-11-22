from flask import Blueprint, flash, redirect, render_template, url_for
from models.cuidador import Cuidador
from models.perro import Perro


cuidador_blueprint = Blueprint('cuidadores', __name__, url_prefix='/cuidadores')


@cuidador_blueprint.route('/')
def index():
    _cuidadores = Cuidador.query.all()
    _list = [_cuidador.to_dict() for _cuidador in _cuidadores]
    return render_template("cuidadores/index.html", cuidadores=_list)


@cuidador_blueprint.route('/<int:id>')
def show(id: int):
    _cuidador = Cuidador.query.get(id)
    _perros_data = Perro.query.filter_by(id_cuidador=id).all()
    _perros = [perro.to_dict() for perro in _perros_data]

    if _cuidador is None:
        flash(f'No se encontro el cuidador con el id {id}', 'error')
        return redirect(url_for('cuidadores.index'))
    return render_template("cuidadores/show.html", cuidador=_cuidador.to_dict(), perros=_perros)
