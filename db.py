from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def restart_db(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
