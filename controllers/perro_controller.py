from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from models.perro import Perro


perro_blueprint = Blueprint('perros', __name__, url_prefix='/perros')


# index
@perro_blueprint.route('/')
@login_required
def index():
    user = current_user
    if user.is_admin:
        _perros = Perro.query.all()
        flash('Esta ruta es visible para los administradores', 'success')
        return render_template("perros/index_admin.html", perros=_perros)
    else:
        flash('Esta ruta es visible solo para los administradores', 'error')
        return render_template("perros/index.html")


# show
@perro_blueprint.route('/<int:id>')
def show(id: int):
    _perro = Perro.query.get(id)
    if _perro is None:
        flash(f'No se encontro el perro con el id {id}', 'error')
        return redirect(url_for('perros.index'))
    return render_template('perros/show.html', perro=_perro)
