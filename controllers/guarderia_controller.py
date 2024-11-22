from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_required
from db import db
from models.cuidador import Cuidador
from models.guarderia import Guarderia
from models.perro import Perro


guarderia_blueprint = Blueprint('guarderias', __name__, url_prefix='/guarderias')


@guarderia_blueprint.route('/')
def index():
    _guarderias = Guarderia.query.all()
    _list = [g.to_dict() for g in _guarderias]
    return render_template("guarderias/index.html", guarderias=_list)


@guarderia_blueprint.route('/<int:id>')
def show(id: int):
    _guarderia = Guarderia.query.get(id)

    _cuidadores_data = Cuidador.query.filter_by(id_guarderia=id).all()
    _cuidadores = [_cuidador.to_dict() for _cuidador in _cuidadores_data]

    _perros_data = Perro.query.filter_by(id_guarderia=id).all()
    _perros = [_perro.to_dict() for _perro in _perros_data]

    if _guarderia is None:
        flash(f'No se encontro la guardería con el id {id}', 'error')
        return redirect(url_for('guarderias.index'))

    return render_template("guarderias/show.html", guarderia=_guarderia.to_dict(), cuidadores=_cuidadores, perros=_perros)


@guarderia_blueprint.route('asignar_cuidador/<int:id>', methods=['GET'])
@login_required
def asignar_cuidador(id: int):
    _cuidador = Cuidador.query.filter_by(id_guarderia=id, nombre='Mario Rodríguez').first()

    if _cuidador is None:
        flash('No se encontro el cuidador Mario Rodríguez en esta guardería :(', 'error')
        return redirect(url_for('guarderias.index'))
    else:
        db.session.query(Perro).filter(Perro.peso < 3, Perro.id_guarderia == id).update({'id_cuidador': _cuidador.id})
        db.session.commit()
        flash('Perros asignados correctamente a Mario Rodríguez ;)', 'success')
        return redirect(url_for('guarderias.index'))
