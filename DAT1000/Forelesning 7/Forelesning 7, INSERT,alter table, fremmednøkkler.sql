-- Om datatyper, INSERT, ALTER TABLE, fremmednøkler

DROP SCHEMA IF EXISTS testdatabase;
CREATE SCHEMA tesdatabase;

USE testdatabase;

CREATE TABLE Datatyper
(
Postnr1 INTEGER
Postnr2 CHAR(4)
Dato1 DATE,
dato2 DATE
);

INSERT INTO Datatyper VALUES(0304,'0304','2022-02-17',20220217);

SELECT *
FROM Datatyper;

CREATE TABLE Telefonliste
(
Mobilnr CHAR(8) PRIMARY KEY,
Fornavn CHAR(15)
);

INSERT INTO Telefonliste VALUES('93031376','Ståle');

ALTER TABLE Telefonliste ADD COLUMN epost CHAR(30);

SELECT *
FROM Telefonliste;

UPDATE Telefonliste
SET epost='stale.vikhagen@usn.no'
WHERE Mobilnr='93031376';

SELECT *
FROM Telefonliste;

CREATE TABLE Postkatalog
(
Postnr CHAR(4) PRIMARY KEY,
Poststed CHAR(20) NOT NULL
);

ALTER TABLE Telefonliste ADD COLUMN Postnr CHAR(4);
ALTER TABLE Telefonliste ADD CONSTRAINT TelefonlistePostkatalogFK FOREIGN KEY
(Postnr) REFERENCES Postkatalog(Postnr);

INSERT INTO Postkatalog VALUES ('3470','Slemmestad');
INSERT INTO Postkatalog VALUES ('6400','Molae');

UPDATE Telefonliste
SET Postnr='3470'
WHERE Mobilnr='93031376';

SELECT *
FROM Telefonliste;

-- Legger til 99999999, Jens på postnr640, ok eller ikke?
INSERT INTO Telefonliste (Mobilnr,Fornavn,Postnr)
VALUES('99999999','Jens','6400');

-- Legger til 44444444, Kari på postnr 7800, ok eller ikke?
INSERT INTO Telefonliste (Mobilnr,Fornavn,Postnr)
VALUES('44444444','Kari','7800');

INSERT INTO Postkatalog VALUES('7800','Namsos');
INSERT INTO Telefonliste (Mobilnr,Fornavn,Postnr)
VALUES('44444444','Kari','7800');

SELECT *
FROM Telefonliste;