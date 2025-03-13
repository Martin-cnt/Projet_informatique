DROP TABLE IF EXISTS animaux;
DROP TABLE IF EXISTS type_animal;

CREATE TABLE type_animal (
    id_type_animal INT AUTO_INCREMENT,
    nom_type VARCHAR(255),
    photo VARCHAR(255),
    PRIMARY KEY(id_type_animal)
);

CREATE TABLE animaux (
    id_animal INT AUTO_INCREMENT,
    type_animal_id INT,  -- Correction ici : type_animal_id doit être INT
    nom_animal VARCHAR(255),
    prix_achat DECIMAL(10, 2),
    date_naissance DATE,
    couleur VARCHAR(50),
    poids DECIMAL(5, 2),
    taille DECIMAL(5, 2),
    photo VARCHAR(255),
    PRIMARY KEY(id_animal),
    FOREIGN KEY(type_animal_id) REFERENCES type_animal(id_type_animal)  -- Ajout de la clé étrangère
);

-- Insertion des enregistrements
INSERT INTO type_animal(id_type_animal, nom_type, photo) VALUES
(NULL, 'chien', 'logo_chien.png'),
(NULL, 'chat', 'logo_chat.png'),
(NULL, 'oiseau', 'logo_oiseau.png'),
(NULL, 'poisson', 'logo_poisson.png');

INSERT INTO animaux(id_animal, type_animal_id, nom_animal, prix_achat, date_naissance, couleur, poids, taille, photo) VALUES
(NULL, 1, 'Snoopy', 100.00, '2021-06-12', 'blanc', 8.43, 40.00, 'Snoopy.jpg'),
(NULL, 1, 'Sam', 50.00, '2023-01-21', 'noir', 12.3, 50.00, 'Sam.jpg'),
(NULL, 1, 'Aaron', 00.00, '2022-11-05', 'roux', 2.43, 10.00, 'Aaron.jpg'),
(NULL, 2, 'Ulysse', 12.32, '2020-12-12', 'blanc', 33, 20.00, 'Ulysse.jpg'),
(NULL, 1, 'Romeo', 150.99, '2021-09-07', 'noir', 2.43, 10.00, 'Romeo.jpg'),
(NULL, 3, 'Abysse', 199.99, '2020-01-21', 'noir', 0.13, 10.00, 'Abysse.jpg'),
(NULL, 1, 'Rox', 299.99, '2020-02-12', 'noir/blanc', 8.43, 60.00, 'Rox.jpg'),
(NULL, 3, 'Donald', 29.9, '2020-02-12', 'noir/blanc', 3.43, 25.00, 'Donald.jpg'),
(NULL, 1, 'Enzo', 299.99, '2020-02-12', 'roux', 8.43, 70.00, 'Enzo.jpg'),
(NULL, 4, 'Nemo', 9.99, '2022-02-12', 'jaune/bleu', 0.1, 11.00, 'Nemo.jpg');

-- Sélection des données pour vérifier
SELECT * FROM animaux;
SELECT * FROM type_animal;






