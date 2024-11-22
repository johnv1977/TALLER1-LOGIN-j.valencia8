-- Inserting data into the table guarderias
INSERT INTO guarderias (nombre, direccion, telefono, logo_url)
VALUES ('La Favorita', 'Av. de las Américas 1020', '+57 333 222 4444', '');

INSERT INTO cuidadores (nombre, telefono, profile_photo_url, id_guarderia)
VALUES ('Ana García', '+34 611223344', '', 1),
       ('Mario Rodríguez', '+34 622334455', '', 1);

INSERT INTO perros (nombre, raza, edad, peso, photo_url, id_guarderia, id_cuidador)
VALUES ('Rufo', 'Labrador', 7, 22.0, 'images\/labrador.jpeg', 1, 1),
       ('Bingo', 'Pug', 2, 6.0, 'images\/pug.jpeg', 1, 1),
       ('Lassie', 'Collie', 5, 27.0, 'images\/collie.jpeg', 1, 1),
       ('Max', 'Pastor Alemán', 3, 30.0, 'images\/pastor_aleman.jpeg', 1, 1),
       ('Lola', 'Chihuahua', 5, 2.5, 'images\/chihuahua.jpeg', 1, 2),
       ('Rocky', 'Boxer', 1, 15.0, 'images\/boxer.jpeg', 1, 2),
       ('Bella', 'Golden Retriever', 7, 32.0, 'images\/golden_retriever.jpeg', 1, 1),
       ('Toby', 'Schnauzer', 4, 10.0, 'images\/schnauzer.jpeg', 1, 3),
       ('Luna', 'Siberiano Husky', 2, 25.0, 'images\/siberiano_husky.jpeg', 1, 1),
       ('Charlie', 'Bulldog', 6, 28.0, 'images\/bulldog.jpeg', 1, 1),
       ('Coco', 'Yorkshire Terrier', 3, 3.5, 'images/yorkshire.jpeg', 1, 1),
       ('Duke', 'Gran Danés', 2, 50.0, 'images/gran_danes.jpeg', 1, 1),
       ('Nina', 'Shih Tzu', 4, 2.5, 'images/shih_tzu.jpeg', 1, 2),
       ('Bolt', 'Husky Siberiano', 1, 20.0, 'images/husky_siberiano.jpeg', 1, 1),
       ('Maya', 'Golden Retriever', 6, 30.0, 'images/golden_retriever.jpeg', 1, 1),
       ('Buddy', 'Beagle', 5, 15.0, 'images/beagle.jpeg', 1, 1),
       ('Zoe', 'Poodle', 2, 2.0, 'images/poodle.jpeg', 1, 2),
       ('Max', 'Rottweiler', 4, 40.0, 'images/rottweiler.jpeg', 1, 1),
       ('Lily', 'Bulldog Francés', 3, 12.0, 'images/bulldog_frances.jpeg', 1, 1),
       ('Charlie', 'Border Collie', 5, 25.0, 'images/border_collie.jpeg', 1, 1),
       ('Bella Lassie', 'Labrador Retriever', 7, 1.5, 'images/labrador_retriever.jpeg', 1, 2),
       ('Rocky', 'Boxer', 1, 18.0, 'images/boxer.jpeg', 1, 1),
       ('Lucy', 'Chihuahua', 2, 2.0, 'images/chihuahua.jpeg', 1, 2),
       ('Duke', 'Doberman', 3, 32.0, 'images/doberman.jpeg', 1, 1),
       ('Daisy', 'Bichon Frise', 4, 5.5, 'images/bichon_frise.jpeg', 1, 1),
       ('Buddy', 'Bull Terrier', 5, 28.0, 'images/bull_terrier.jpeg', 1, 1),
       ('Molly', 'Golden Retriever', 6, 31.0, 'images/golden_retriever.jpeg', 1, 1),
       ('Bailey', 'Beagle', 3, 13.0, 'images/beagle.jpeg', 1, 1),
       ('Sophie', 'Poodle', 2, 7.5, 'images/poodle.jpeg', 1, 1),
       ('Charlie', 'Rottweiler', 4, 38.0, 'images/rottweiler.jpeg', 1, 1);
