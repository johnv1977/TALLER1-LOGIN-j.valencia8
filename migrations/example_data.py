from models.cuidador import Cuidador
from models.guarderia import Guarderia
from models.perro import Perro
from models.user import User


def data_cuidadores(app, db):
    with app.app_context():
        # Cuidadores
        _cuidadores = [
            Cuidador(
                nombre='Ana García',
                telefono='+57 311 222 3333',
                profile_photo_url='',
                id_guarderia=1
            ),
            Cuidador(
                nombre='Mario Rodríguez',
                telefono='+57 322 444 5555',
                profile_photo_url='',
                id_guarderia=1
            ),
            Cuidador(
                nombre='Catalina Forero',
                telefono='+57 311 666 7777',
                profile_photo_url='',
                id_guarderia=2
            ),
            Cuidador(
                nombre='Santiago Valencia',
                telefono='+57 322 888 9999',
                profile_photo_url='',
                id_guarderia=2
            )

        ]
        for cuidador in _cuidadores:
            db.session.add(cuidador)
            db.session.commit()


def data_guarderia(app, db):
    with app.app_context():
        # Guarderías
        guarderia = Guarderia(
            nombre='La Favorita',
            direccion='Av. de las Américas 1020',
            telefono='+57 333 222 4444',
            logo_url=''
        )
        db.session.add(guarderia)
        guarderia = Guarderia(
            nombre='Otra guardería',
            direccion='Av. Boyacá 3040',
            telefono='+57 333 444 8888',
            logo_url=''
        )
        db.session.add(guarderia)
        db.session.commit()


def data_perros(app, db):
    with app.app_context():
        # Perros
        perros = [
            # Guardería 1
            Perro(
                nombre='Rufo',
                raza='Labrador',
                edad=7,
                peso=2.2,
                photo_url='',
                id_guarderia=1,
                id_cuidador=1
            ),
            Perro(
                nombre='Bingo',
                raza='Pug',
                edad=2,
                peso=6.0,
                photo_url='',
                id_guarderia=1,
                id_cuidador=1
            ),
            Perro(
                nombre='Lassie',
                raza='Collie',
                edad=5,
                peso=2.7,
                photo_url='',
                id_guarderia=1,
                id_cuidador=1
            ),
            Perro(
                nombre='Max',
                raza='Pastor Alemán',
                edad=3,
                peso=3.0,
                photo_url='',
                id_guarderia=1,
                id_cuidador=1
            ),
            Perro(
                nombre='Lola',
                raza='Chihuahua',
                edad=5,
                peso=2.5,
                photo_url='',
                id_guarderia=1,
                id_cuidador=1
            ),
            Perro(
                nombre='Rocky',
                raza='Boxer',
                edad=1,
                peso=1.75,
                photo_url='',
                id_guarderia=1,
                id_cuidador=1
            ),
            Perro(
                nombre='Bella',
                raza='Golden Retriever',
                edad=7,
                peso=3.2,
                photo_url='',
                id_guarderia=1,
                id_cuidador=1
            ),
            Perro(
                nombre='Toby',
                raza='Schnauzer',
                edad=4,
                peso=1.0,
                photo_url='',
                id_guarderia=1,
                id_cuidador=1
            ),
            Perro(
                nombre='Luna',
                raza='Siberiano Husky',
                edad=2,
                peso=2.5,
                photo_url='',
                id_guarderia=1,
                id_cuidador=1
            ),
            Perro(
                nombre='Charlie',
                raza='Bulldog',
                edad=6,
                peso=2.8,
                photo_url='',
                id_guarderia=1,
                id_cuidador=1
            ),
            Perro(
                nombre='Coco',
                raza='Yorkshire Terrier',
                edad=3,
                peso=3.5,
                photo_url='',
                id_guarderia=1,
                id_cuidador=1
            ),
            Perro(
                nombre='Duke',
                raza='Gran Danés',
                edad=2,
                peso=5.0,
                photo_url='',
                id_guarderia=1,
                id_cuidador=1
            ),
            Perro(
                nombre='Nina',
                raza='Shih Tzu',
                edad=4,
                peso=2.5,
                photo_url='',
                id_guarderia=1,
                id_cuidador=1
            ),
            Perro(
                nombre='Bolt',
                raza='Husky Siberiano',
                edad=1,
                peso=2.0,
                photo_url='',
                id_guarderia=1,
                id_cuidador=1
            ),
            Perro(
                nombre='Maya',
                raza='Golden Retriever',
                edad=6,
                peso=3.0,
                photo_url='',
                id_guarderia=1,
                id_cuidador=1
            ),
            # Guardería 2
            Perro(
                nombre='Buddy',
                raza='Beagle',
                edad=5,
                peso=1.5,
                photo_url='',
                id_guarderia=2,
                id_cuidador=3
            ),
            Perro(
                nombre='Zoe',
                raza='Poodle',
                edad=2,
                peso=2.0,
                photo_url='',
                id_guarderia=2,
                id_cuidador=3
            ),
            Perro(
                nombre='Max',
                raza='Rottweiler',
                edad=4,
                peso=4.0,
                photo_url='',
                id_guarderia=2,
                id_cuidador=3
            ),
            Perro(
                nombre='Lily',
                raza='Bulldog Francés',
                edad=3,
                peso=1.2,
                photo_url='',
                id_guarderia=2,
                id_cuidador=3
            ),
            Perro(
                nombre='Charlie',
                raza='Border Collie',
                edad=5,
                peso=2.5,
                photo_url='',
                id_guarderia=2,
                id_cuidador=3
            ),
            Perro(
                nombre='Bella Lassie',
                raza='Labrador Retriever',
                edad=7,
                peso=1.5,
                photo_url='',
                id_guarderia=2,
                id_cuidador=3
            ),
            Perro(
                nombre='Rocky',
                raza='Boxer',
                edad=1,
                peso=1.8,
                photo_url='',
                id_guarderia=2,
                id_cuidador=3
            ),
            Perro(
                nombre='Lucy',
                raza='Chihuahua',
                edad=2,
                peso=2.0,
                photo_url='',
                id_guarderia=2,
                id_cuidador=3
            ),
            Perro(
                nombre='Duke',
                raza='Doberman',
                edad=3,
                peso=3.2,
                photo_url='',
                id_guarderia=2,
                id_cuidador=3
            ),
            Perro(
                nombre='Daisy',
                raza='Bichon Frise',
                edad=4,
                peso=5.5,
                photo_url='',
                id_guarderia=2,
                id_cuidador=3
            ),
            Perro(
                nombre='Buddy',
                raza='Bull Terrier',
                edad=5,
                peso=2.8,
                photo_url='',
                id_guarderia=2,
                id_cuidador=3
            ),
            Perro(
                nombre='Molly Lassie',
                raza='Golden Retriever',
                edad=6,
                peso=3.1,
                photo_url='',
                id_guarderia=2,
                id_cuidador=3
            ),
            Perro(
                nombre='Bailey',
                raza='Beagle',
                edad=3,
                peso=1.3,
                photo_url='',
                id_guarderia=2,
                id_cuidador=3
            ),
            Perro(
                nombre='Sophie',
                raza='Poodle',
                edad=2,
                peso=7.5,
                photo_url='',
                id_guarderia=2,
                id_cuidador=3
            ),
            Perro(
                nombre='Charlie',
                raza='Rottweiler',
                edad=4,
                peso=3.8,
                photo_url='',
                id_guarderia=2,
                id_cuidador=3
            )
        ]

        for perro in perros:
            db.session.add(perro)
            db.session.commit()


def data_users(app, db):
    with app.app_context():
        # Usuarios
        users = [
            User(
                username='catalina',
                password='123',
                profile_photo_url='',
                is_admin=False
            ),
            User(
                username='juan.pablo',
                password='123',
                profile_photo_url='',
                is_admin=False
            ),
            User(
                username='admin',
                password='123',
                profile_photo_url='',
                is_admin=True
            )
        ]
        for user in users:
            db.session.add(user)
            db.session.commit()
