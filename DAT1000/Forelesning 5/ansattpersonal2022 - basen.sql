DROP SCHEMA IF EXISTS ansattpersonal2022;
CREATE SCHEMA ansattpersonal2022;

USE ansattpersonal2022;

CREATE TABLE Stillingstype
(
Stillingskode CHAR(4),
Stillingsbetegnelse CHAR(20),
CONSTRAINT StillingstypePK PRIMARY KEY(Stillingskode)
);

CREATE TABLE Avdeling
(
Avdelingsnr CHAR(4),
Avdelingsnavn CHAR(20),
CONSTRAINT AvdelingPK PRIMARY KEY(Avdelingsnr)
);

CREATE TABLE Kurs
(
Kursnr CHAR(4),
Kursnavn CHAR(20),
CONSTRAINT KursPK PRIMARY KEY(Kursnr)
);

CREATE TABLE Postkatalog
(
Postnr CHAR(4),
Poststed CHAR(20),
CONSTRAINT PostkatalogPK PRIMARY KEY(Postnr)
);

CREATE TABLE Ansatt
(
Ansattnr CHAR(4),
Fornavn CHAR(15),
Etternavn CHAR(20),
Gateadresse CHAR(25),
Telefonnr CHAR(8),
Stillingskode CHAR(4),
Avdelingsnr CHAR(4),
Postnr CHAR(4),
CONSTRAINT AnsattPK PRIMARY KEY(Ansattnr),
CONSTRAINT AnsattStillingstypeFK FOREIGN KEY(Stillingskode) REFERENCES Stillingstype(Stillingskode),
CONSTRAINT AnsattAvdelingFK FOREIGN KEY(Avdelingsnr) REFERENCES Avdeling(Avdelingsnr),
CONSTRAINT AnsattPostkatalogFK FOREIGN KEY(Postnr) REFERENCES Postkatalog(Postnr)
);

CREATE TABLE Kursdeltagelse
(
Ansattnr CHAR(4),
Kursnr CHAR(4),
Dato DATE,
Vurdering CHAR(20),
CONSTRAINT KursdeltagelsePK PRIMARY KEY(Ansattnr,Kursnr,Dato),
CONSTRAINT KursdeltagelseAnsattFK FOREIGN KEY(Ansattnr) REFERENCES Ansatt(Ansattnr),
CONSTRAINT KursdeltagelseKursFK FOREIGN KEY(Kursnr) REFERENCES Kurs(Kursnr)
);