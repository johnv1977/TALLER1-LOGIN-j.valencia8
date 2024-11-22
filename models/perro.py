from models.animal import Animal
from db import db


class Perro(Animal):
    '''
    Representa a un animal.
    Args:
        nombre (str): Nombre del animal.
        edad (int): Edad del animal en años.
        peso (float): Peso del animal en kilogramos.
    '''

    __tablename__ = 'perros'

    def __init__(self, nombre: str, edad: int, peso: float, photo_url: str, raza: str, id_guarderia: int, id_cuidador: int) -> None:
        super().__init__(nombre, edad, peso, photo_url, id_guarderia, id_cuidador)
        self.raza = raza

    raza = db.Column(db.String(35), nullable=False)

    def from_dict(self, data) -> None:
        print(data)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'edad': self.edad,
            'peso': self.peso,
            'raza': self.raza,
            'photo_url': self.photo_url,
            'id_guarderia': self.id_guarderia,
            'id_cuidador': self.id_cuidador,
        }

    @staticmethod
    def perros_por_nombre(nombre: str) -> list:
        # _perros_data = db.session.execute(db.select(Perro).where(Perro.nombre == nombre))
        _perros_data = Perro.query.filter(Perro.nombre.like(f'%{nombre}%'))
        _perros = [perro.to_dict() for perro in _perros_data]
        return _perros
