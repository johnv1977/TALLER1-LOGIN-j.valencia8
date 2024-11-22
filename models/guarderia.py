from sqlalchemy import text
from db import db


class Guarderia(db.Model):
    __tablename__ = 'guarderias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(150), nullable=False)
    telefono = db.Column(db.String(25), nullable=False)
    logo_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime,
                           nullable=False,
                           default=db.func.current_timestamp(),
                           server_default=text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.DateTime,
                           nullable=False,
                           default=db.func.current_timestamp(),
                           server_default=text('CURRENT_TIMESTAMP'),
                           onupdate=db.func.current_timestamp())

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'logo_url': self.logo_url
        }
