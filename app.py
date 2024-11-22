from flask import Flask
from config import app_config_db, app_config_global_vars
from login import app_config_login
from db import db, restart_db
from controllers.app_controller import app_blueprint, define_error_handlers
from controllers.cuidador_controller import cuidador_blueprint
from controllers.guarderia_controller import guarderia_blueprint
from controllers.perro_controller import perro_blueprint
from controllers.user_controller import user_blueprint
from migrations.example_data import data_cuidadores, data_guarderia, data_perros, data_users


# Iniciar y configurar la aplicación
app = Flask(__name__, template_folder="views")
app_config_db(app)
app_config_login(app)

# Iniciar la base de datos
db.init_app(app)
restart_db(app)

# Insertar datos de ejemplos
data_guarderia(app, db)
data_cuidadores(app, db)
data_perros(app, db)
data_users(app, db)

# Registrar las rutas
app.register_blueprint(app_blueprint)
app.register_blueprint(cuidador_blueprint)
app.register_blueprint(guarderia_blueprint)
app.register_blueprint(perro_blueprint)
app.register_blueprint(user_blueprint)

# Definir manejadores de errores en las rutas
define_error_handlers(app)

# Definir variables globales
app_config_global_vars(app)


if __name__ == "__main__":
    app.run(debug=True)
