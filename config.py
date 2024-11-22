import os
from dotenv import load_dotenv
from flask import url_for


load_dotenv()

login_manager = None


def app_config_db(app):
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    db_string_connection = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

    app.config['SQLALCHEMY_DATABASE_URI'] = db_string_connection
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_BINDS'] = {
        'perros': db_string_connection,
        'cuidadores': db_string_connection,
        'guarderias': db_string_connection
    }


def app_config_global_vars(app):
    @app.context_processor
    def inject_global_vars():
        return dict(
            site_name=os.getenv('APP_NAME'),
            menu_items=app_menu_items()
        )

    return app


def app_menu_items():
    return [
        {'name': 'Inicio', 'url': url_for('app.index')},
        {'name': 'Guarderías', 'url': url_for('guarderias.index')},
        {'name': 'Cuidadores', 'url': url_for('cuidadores.index')},
        {'name': 'Perros', 'url': url_for('perros.index')},
        {'name': 'Logout', 'url': url_for('users.logout')},
    ]
