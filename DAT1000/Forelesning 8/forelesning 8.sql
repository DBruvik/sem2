-- Grunnstrukturen for SELECT
-- SELECT
-- FROM
-- WHERE
-- GROUP BY
-- HAVING
-- ORDER BY

-- Lekse fra forelesning 7:
-- Gullklubben, spørring og senere  VIEW for å plukke ut kunder med 10 eller flere bestillinger
-- Gullklubblista,"liste til sjefen" med informasjon om alle kunder i gullklubben
-- med info om alle kunder i "Gullklubben" basert på VIEW'et og tabellene Kunde og Poststed

USE Hobbyhuset; 
-- Gullklubben og gullklubblista
SELECT KNr, COUNT(*) AS AntallBestillinger
FROM Ordre
GROUP BY KNr
HAVING AntallBestillinger>=10;

-- som VIEW
CREATE VIEW Gullklubben AS
(
SELECT KNr, COUNT(*) AS AntallBestillinger
FROM Ordre
GROUP BY KNr
HAVING AntallBestillinger>=10
);

SELECT * 
FROM Gullklubben;

-- Gullklubblista
SELECT Gullklubben.KNr,Fornavn,Etternavn,Adresse,Kunde.Postnr,Poststed,AntallBestillinger
FROM Gullklubben,Kunde,Poststed
WHERE Gullklubben.KNr=Kunde.KNr AND Kunde.Postnr=Poststed.Postnr;

-- Som view
CREATE VIEW Gullklubblista AS
(
SELECT Gullklubben.KNr,Fornavn,Etternavn,Adresse,Kunde.Postnr,Poststed,Antallbestillinger
FROM Gullklubben,Kunde,Poststed
WHERE Gullklubben.KNr=Kunde.KNr AND Kunde.Postnr=Poststed.Postnr
);

SELECT *
FROM Gulklubblista;

SELECT *
FROM Gullklubblista
ORDER BY AntallBestillinger DESC;

-- Oppgave
-- Gullklubblista som en spørring uten bruk av view
-- Tips: Pass på gruppekriterier

SELECT Ordre.KNr, Fornavn,Etternavn,Adresse,Kunde.Postnr,Poststed, COUNT(*) AS Antallbestillinger
FROM Kunde,Poststed,Ordre
WHERE Kunde.KNr=Ordre.KNr AND Kunde.Postnr=Poststed.Postnr
GROUP BY Ordre.KNr,Fornavn,Etternavn,Adresse,Kunde.Postnr,Poststed
HAVING Antallbestillinger>=10
ORDER BY Antallbestillinger;

-- --------------------------------------------------------------------------------------------------------------
-- Egenkobling
-- Du kan lage databasen på følgende måte
-- 1) Kopier tabelldefinisjonen Ansatt fra Hobbyhuset
-- og legg til kolonnen leder, smallint(6)
-- Fjern definisjonen av fremmednøkkelen på postnr
-- Legg til fremmednøkkel Leder som refererer til Ansatt(Ansattnr)
-- Men da må du gjøre om på indatarekkefølgen slik at sjefene er registrert
-- før de leder
-- 2) Kopier inndatasetningene fra hobbyhuset
-- Legg inn leder for hver ansatt tilsvarende figur 4.6 s104("Endre hver inndatasetning")
DROP SCHEMA IF EXISTS Egenkobling;
CREATE SCHEMA Egenkobling;

USE Egenkobling;

CREATE TABLE Ansatt
(
  AnsNr       SMALLINT,
  Fornavn     VARCHAR(50) NOT NULL,
  Etternavn   VARCHAR(50) NOT NULL,
  Adresse     VARCHAR(100),
  PostNr      CHAR(4) NOT NULL,
  Fødselsdato DATE,
  Kjønn       CHAR(1),
  Stilling    VARCHAR(50),
  Årslønn     DECIMAL(8,2) NOT NULL,
  Leder       SMALLINT,
  CONSTRAINT  AnsattPN PRIMARY KEY (AnsNr),
  CONSTRAINT  LederAnsattFK FOREIGN KEY (Leder) REFERENCES Ansatt(AnsNr)
);

INSERT INTO Ansatt (AnsNr, Fornavn, Etternavn, Adresse, PostNr, Fødselsdato, Kjønn, Stilling, Årslønn,Leder) VALUES
(2, 'Gunnlaug', 'Angeltveit', 'Langmyrgrenda 9', '3800', '1969-03-29', 'K', 'Markedssjef', '643200.00',NULL),
(7, 'Henriette', 'Brobakken', 'Stubberud Sognsvann 1', '3800', '1971-10-01', 'K', 'Daglig leder', '833800.00','2'),
(8, 'Synøve', 'Bakketun', 'Vassøyveien 7', '3840', '1985-05-15', 'K', 'Kundebehandler', '518100.00','2'),
(1, 'Georg', 'Barth', 'Kringsjågrenda 3F', '3841', '1982-10-20', 'M', 'Lagerleder', '604900.00','2'),
(3, 'Morgan', 'Dalland', 'Jansbergveien 19', '3830', '1974-01-10', 'M', 'Innkjøper', '670500.00','7'),
(6, 'Vilde', 'Aksnes', 'Minister Ditleffs vei 44', '3810', '1977-10-11', 'K', 'Databaseadministrator', '693200.00','8'),
(9, 'Ragnvald', 'Allum', 'Utsikten 4', '3812', '1992-03-07', 'M', 'Kundebehandler', '484700.00','7'),
(11, 'Oliver', 'Abrahamsen', 'Tarjei Vesaas\' vei 3A', '3812', '1989-01-20', 'M', 'Lagermedarbeider', '466900.00','7'),
(13, 'Oda', 'Cappelen', 'Norheimskneiken 12', '3800', '1991-02-28', 'K', 'Produktutvikler', '653100.00','8'),
(16, 'Andrine', 'Ebbesen', 'Kristianias gate 9', '3800', '1988-12-27', 'K', 'Regnskapssekretær', '532300.00','7');


SELECT AnsNr, Fornavn, Etternavn, Leder
FROM Ansatt;
-- Alle ansatte med navn på leder
SELECT Ansatte.AnsNr,Ansatte.Etternavn,Ansatte.Fornavn,Lederen.Etternavn AS HarSomLeder
FROM Ansatt As Ansatte, Ansatt AS Lederen
WHERE Ansatte.Leder=Lederen.AnsNr
ORDER BY HarSomLeder,Ansatte.Etternavn,Ansatte.Fornavn;

-- Oppgave:
-- Lag SQL-setning slik at du også får med de ansatte som ikke har leder
SELECT Ansatte.AnsNr,Ansatte.Etternavn,Ansatte.Fornavn,Lederen.Etternavn AS Leder
FROM Ansatt As Ansatte, Ansatt AS Lederen
WHERE Ansatte.Leder=Lederen.AnsNr
ORDER BY Leder,Ansatte.Etternavn,Ansatte.Fornavn;

SELECT Ansatte.AnsNr,Ansatte.Etternavn,Ansatte.Fornavn,Lederen.Etternavn AS Leder 
FROM (Ansatt As Ansatte) LEFT OUTER JOIN (Ansatt AS Lederen)
ON Ansatte.Leder=Lederen.AnsNr
ORDER BY Leder,Ansatte.Etternavn,Ansatte.Fornavn;


-- View for produksjon av salgsrapport
-- Oppgaver:
-- Bruk view'et sammen med andre tabeller for å lage ulike salgsrapporter

USE Hobbyhuset;
CREATE VIEW Salg AS
(
SELECT OL.*,V.Betegnelse,K.Navn AS Kategori,O.OrdreDato,O.Knr
FROM Ordre AS O, Ordrelinje AS OL,Vare AS V,Kategori AS K
WHERE OL.OrdreNr=O.OrdreNr
	AND OL.VNr=V.VNr
    AND V.KatNr=K.KatNr
);
    
SELECT *
FROM Salg;

SELECT *
FROM Ordrelinje;

-- Kunder uten bestillinger ved bruk av NOT EXIST
SELECT *
FROM Kunde
WHERE NOT EXISTS
	(SELECT KNr FROM Ordre
    WHERE Kunde.KNr=Ordre.KNr);
    
-- Kunder med bestillinger ved bruk av EXISTS
SELECT *
FROM Kunde
WHERE EXISTS
	(SELECT KNr FROM Ordre
    WHERE Kunde.KNr=Ordre.KNr);
    
-- Natural JOIN brukes(anbefales ikke)
USE ansattpersonal2022;
SELECT *
FROM Ansatt NATURAL JOIN Stillingstype;

SELECT *
FROM Ansatt NATURAL JOIN Stillingstype NATURAL JOIN Avdeling;

-- Mer om del-såærringer
-- varer billigere enn gjennomsnittet
USE hobbyhuset;
SELECT VNr, Betegnelse, Pris
FROM VARE
WHERE Pris<(SELECT AVG(Pris) FROM Vare);

-- Vekselvirkende delspørringer
-- Billigste vare i hver kategori, alternativ 1
SELECT Vare1.VNr, Vare1.Betegnelse, Vare1.KatNr,Vare1.Pris
FROM Vare AS Vare1
WHERE Vare1.Pris=
	(SELECT MIN(Vare2.Pris)
    FROM Vare AS Vare2
		WHERE Vare1.KatNr=Vare2.KatNr);
        
-- Oppgaver:
-- 1) løsning ved bruk av view (alternativ 2)
-- View for billigesteIKategori
-- 2) BIlligsteIKategori som navngitt spørring og spørring i FROM-delen (alternativ3)

DROP VIEW IF EXISTS BilligsteIKategori;
CREATE VIEW BilligsteIKategori AS
(
SELECT KatNr, MIN(Pris) AS Billigste
FROM Vare
GROUP BY KatNr
);

SELECT *
FROM BilligsteIKategori;

SELECT VNr, Betegnelse, Pris, Vare.KatNr
FROM Vare, BilligsteIKategori
WHERE Vare.KatNr=BilligsteIKategori.KatNr
	AND Vare.Pris=BilligsteIKategori.Billigste;
    
-- BilligsteIKategori som navngitt spørring og spørring i FROM-Delen
SELECT VNr,Betegnelse,Pris,Vare.KatNr
FROM Vare,(SELECT KatNr,MIN(Pris) AS Billigste
			FROM VARE
			GROUP BY KatNr) AS BiK
WHERE Vare.KatNr=BiK.KatNr
	AND Vare.Pris=BiK.Billigste;
