from sqlalchemy import text
from db import db


class Animal(db.Model):
    '''
    Representa a un animal.
    Args:
        nombre (str): Nombre del animal.
        edad (int): Edad del animal en años.
        peso (float): Peso del animal en kilogramos.
        photo_url (str): URL de la foto del animal.
        id_guarderia (int): ID de la guardería donde reside el animal.
        id_cuidador (int): ID del cuidador que cuida el animal.
    '''

    def __init__(self, nombre: str, edad: int, peso: float, photo_url: str, id_guarderia: int, id_cuidador: int) -> None:
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.photo_url = photo_url
        self.id_guarderia = id_guarderia
        self.id_cuidador = id_cuidador

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(75), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    photo_url = db.Column(db.String(255), nullable=True)
    id_guarderia = db.Column(db.Integer, db.ForeignKey('guarderias.id'))
    id_cuidador = db.Column(db.Integer, db.ForeignKey('cuidadores.id'))
    created_at = db.Column(db.DateTime,
                           nullable=False,
                           default=db.func.current_timestamp(),
                           server_default=text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.DateTime,
                           nullable=False,
                           default=db.func.current_timestamp(),
                           server_default=text('CURRENT_TIMESTAMP'),
                           onupdate=db.func.current_timestamp())
