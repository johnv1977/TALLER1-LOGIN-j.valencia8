from sqlalchemy import text
from db import db


class Cuidador(db.Model):
    __tablename__ = 'cuidadores'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(25), nullable=False)
    profile_photo_url = db.Column(db.String(255), nullable=True)
    id_guarderia = db.Column(db.Integer, db.ForeignKey('guarderias.id'))
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
            'telefono': self.telefono,
            'profile_photo_url': self.profile_photo_url,
            'id_guarderia': self.id_guarderia
        }
