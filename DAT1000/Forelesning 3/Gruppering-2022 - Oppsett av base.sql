DROP SCHEMA IF EXISTS gruppering2022;
CREATE SCHEMA gruppering2022;

USE gruppering2022;

CREATE TABLE Ansatt
(
Ansattnr CHAR(4),
Fornavn CHAR(15) NOT NULL,
Stillingskode CHAR(4),
Lønnstrinn CHAR(2),
Avdelingsnr CHAR(4),
CONSTRAINT AnsattPK PRIMARY KEY (Ansattnr)
);

INSERT INTO Ansatt VALUES ('1','Brit','1008','66','3');
INSERT INTO Ansatt VALUES ('2','Karl','2000','66','2');
INSERT INTO Ansatt VALUES ('4','Berit','1001','67','4');
INSERT INTO Ansatt VALUES ('7','Jonas','1001','54','1');
INSERT INTO Ansatt VALUES ('5','Kari','1337','69','5');
INSERT INTO Ansatt VALUES ('8','Marthe','1551','60','4');
-- resten fyller du ut
-- flere ansatte på samme/forskjellige lønnstrinn på samme/forskjellige stillingskoder på samme/forskjellige avdelinger
