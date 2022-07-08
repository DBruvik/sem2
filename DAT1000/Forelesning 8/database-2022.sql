-- Introduksjon DDL, opprette database, opprette tabell, legge inn data

-- Skript for å
-- opprette databasen
-- opprette tabellen
-- legge til data

-- Sletter databasen hvis den finnes
DROP SCHEMA IF EXISTS nydatabase;
-- Oppretter databasen
CREATE SCHEMA IF NOT EXISTS nydatabase;

USE nydatabase;

-- Oppretter tabellen Vare
-- variant av CREATE-setning s 66,
-- forbyr NULL-merker i enkelte kolonner
CREATE TABLE Vare
(
VNr CHAR(5) PRIMARY KEY,
Betegnelse VARCHAR(30) NOT NULL,
Pris DECIMAL(8,2) NOT NULL,
KatNr SMALLINT NOT NULL,
Antall INTEGER NOT NULL,
Hylle CHAR(3)
);

-- legge inn data i tabellen vare, vare nr 1
INSERT INTO Vare(VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('90693','Marsipantang',57.00,4,0,'B17');

-- her legger dere inn vare nr 2 i tabellen s 67
INSERT INTO Vare(VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('44939','Hobbymaling, 6 farger',115.00,2,2,'B02');
-- vare nr 3
INSERT INTO Vare(VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('10830','Nisseskjegg, 30 cm',57.50,13,42,NULL);

-- her legger dere inn vare nr 4 tom vare nr 8 etter samme struktur
INSERT INTO Vare(VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('33044','Blandet blomsterfrø',14.50,15,1080,'E05');
INSERT INTO Vare(VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('15217','Kram tørrfluekorker, 5stk',32.00,7,213,'B42');
INSERT INTO Vare(VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('90164','Lakrisekstrakt, 100g',75.50,4,104,'B06');
INSERT INTO Vare(VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('15207','Antron garn, hvit',24.50,7,21,'B41');
INSERT INTO Vare(VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('13001','Glasskuler, 100 gr',38.00,13,0,'E11');
-- vare nr 9
-- trenger ikke feltnavnlista hvis data i alle felt
INSERT INTO Vare VALUES('21032','Furuspon 3 cm',57.50,17,240,'B32');

-- her legger dere inn vare nr 10 tom 15, kortform
INSERT INTO Vare VALUES('33045','Blomkarse',17.50,15,1206,'E05');
INSERT INTO Vare VALUES('55130','Moro med marsipan',298.50,10,140,'C20');
INSERT INTO Vare VALUES('15211','Tubeflue verktøy',209.00,7,39,'B42');
INSERT INTO Vare VALUES('42615','Gipsform marihøner',106.00,3,124,'B03');
INSERT INTO Vare VALUES('64551','Hengebegonia, 10 stk.',118.00,16,206,NULL);
INSERT INTO Vare VALUES('65247','Liten plantespade',75.00,1,76,'A25');

SELECT *
FROM Vare;
