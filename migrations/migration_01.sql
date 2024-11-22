CREATE TABLE guarderias (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50),
    direccion VARCHAR(150),
    telefono VARCHAR(25),
    logo_url VARCHAR(255) NULL DEFAULT '',
    PRIMARY KEY (id)
);


CREATE TABLE cuidadores (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50),
    telefono VARCHAR(25),
    profile_photo_url VARCHAR(255) NULL DEFAULT '',
    id_guarderia INT,
    PRIMARY KEY (id),
    FOREIGN KEY (id_guarderia) REFERENCES guarderias(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


CREATE TABLE perros (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(75) NOT NULL,
    raza VARCHAR(35),
    edad INT,
    peso DECIMAL(5,2),
    photo_url VARCHAR(255) NULL DEFAULT '',
    id_guarderia INT,
    id_cuidador INT,
    PRIMARY KEY (ID),
    FOREIGN KEY (id_guarderia) REFERENCES guarderias(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_cuidador) REFERENCES cuidadores(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);


SELECT * FROM perros WHERE nombre LIKE '%Lassie%';


UPDATE perros SET id_cuidador = 2 WHERE peso < 3;


SELECT * FROM guarderias WHERE guarderias.nombre = 'La Favorita';


SELECT * FROM perros WHERE id_guarderia IN (SELECT id FROM guarderias WHERE nombre = 'La Favorita');


SELECT * FROM cuidadores WHERE id_guarderia IN (SELECT id FROM guarderias WHERE nombre = 'La Favorita');

