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

-- vare nr 3
INSERT INTO Vare(VNr,Betegnelse,Pris,KatNr,Antall,Hylle) VALUES('10830','Nisseskjegg, 30 cm',57.50,13,42,NULL);

-- her legger dere inn vare nr 4 tom vare nr 8 etter samme struktur

-- vare nr 9
-- trenger ikke feltnavnlista hvis data i alle felt
INSERT INTO Vare VALUES('21032','Furuspon 3 cm',57.50,17,240,'B32');

-- her legger dere inn vare nr 10 tom 15, kortform

SELECT *
FROM Vare;
