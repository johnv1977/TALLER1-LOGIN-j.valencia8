import os
from flask import Flask, render_template
from flask_login import LoginManager, login_required

app = Flask(__name__)

secret_key = os.urandom(24)
app.config["SECRET_KEY"] = secret_key

login_manager = LoginManager(app)


@app.route('/ruta-logueada')
@login_required
def ruta():
    return render_template("ruta-logueada.html")
