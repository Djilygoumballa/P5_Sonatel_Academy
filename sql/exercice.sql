--EXERCICE1

                --1ER CAS
CREATE DATABASE Piece_vehicule;
USE Piece_vehicule;
CREATE TABLE Vehicule (
    VIN              INT(7) AUTO_INCREMENT PRIMARY KEY,
    marque                   VARCHAR(15),
    modele                   VARCHAR(15),
    annee                    INT(4)
);

CREATE TABLE Reference (
    id_ref                  INT(7) AUTO_INCREMENT PRIMARY KEY,

);

CREATE TABLE Piece (
    id_piece                INT(7) AUTO_INCREMENT PRIMARY KEY,
    date_recuparation       DATE,
    id_ref                  INT,
    FOREIGN KEY (id_ref) REFERENCES Reference(id_ref)
);

CREATE TABLE Correspondance_vehicule_piece (
    id_vehicule                 INT,
    id_piece                    INT,
    FOREIGN KEY (VIN) REFERENCES Vehicule(VIN),
    FOREIGN KEY (id_piece) REFERENCES Piece(id_piece)
);