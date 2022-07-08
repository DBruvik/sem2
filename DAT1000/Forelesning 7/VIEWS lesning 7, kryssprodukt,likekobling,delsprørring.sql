USE ansattpersonal2022;

-- Dersom vi har kjørt skript for databasen på nytt,
-- må vi huske å kjøre CREATE VIEW Ansattliste fra forelesning 6 før vi lager spørringen

SELECT *
FROM Ansatt
ORDER BY Etternavn;

-- KRYSSPRODUKT
SELECT *
FROM Ansatt INNER JOIN Postkatalog;

SELECT *
FROM Ansatt JOIN Postkatalog;

-- Likekobling
SELECT Ansattnr,Fornavn,Etternavn,Gateadresse,Ansatt.Postnr,Poststed
FROM Ansatt JOIN Postkatalog
	ON Ansatt.Postnr=Postkatalog.Postnr;

SELECT Ansattnr,Fornavn,Etternavn,Gateadresse,Ansatt.Postnr,Poststed
FROM Ansatt JOIN Postkatalog
		USING(Postnr);

SELECT Etternavn,Fornavn,Stillingsbetegnelse,Avdelingsnavn
FROM Stillingstype JOIN
	(Ansatt JOIN Avdeling
		USING(Avdelingsnr))
	USING(Stillingskode);

-- Ytre koblinger
SELECT *
FROM Stillingstype LEFT JOIN Ansatt
	ON Stillingstype.Stillingskode=Ansatt.Stillingskode;

SELECT *
FROM Stillingstype LEFT JOIN Ansatt
	USING(Stillingskode);

-- Algoritmeforklaringer
USE Hobbyhuset;
-- Første SELECT'n s102
SELECT Ordre.*, Fornavn,Etternavn,Poststed
FROM Ordre,Kunde,Poststed
WHERE Ordre.Knr=Kunde.KNr
	AND Kunde.Postnr=Poststed.Postnr;

-- Siste SELECT'n s103
SELECT Kunde.KNr,Etternavn,COUNT(*) AS AntallOrdre
FROM Kunde,Ordre
WHERE Kunde.KNr=Ordre.KNr
GROUP BY Kunde.KNr,Etternavn;

-- Utvidet med gruppebetingelse
SELECT Kunde.KNr,Etternavn,COUNT(*) AS AntallOrdre
FROM Kunde,Ordre
WHERE Kunde.KNr=Ordre.KNr
GROUP BY Kunde.KNr,Etternavn
HAVING AntallOrdre>=10;

-- Kortnavn/Alias
SELECT K.KNr,Etternavn,COUNT(*) AS AntallOrdre
FROM Kunde AS K, Ordre AS O
WHERE K.KNr=O.KNr
GROUP BY K.KNr,Etternavn
HAVING AntallOrdre>=10;

-- Introduksjon til del-spørringer, del-sporringer i betingelser
USE Hobbyhuset;
SELECT *
FROM Kunde;

SELECT *
FROM Kategori;

-- Hvem har "bestilt varer"?
SELECT * 
FROM Kunde
WHERE KNr IN (SELECT KNr FROM Ordre);

-- Kunder som aldri har bestilt
SELECT * 
FROM Kunde
WHERE KNr NOT IN(SELECT KNr FROM Ordre);

-- View'et GodeKunder
CREATE VIEW GodeKunder AS(
SELECT *
FROM Kunde
WHERE KNr IN
	(SELECT Knr FROM Ordre)
);

-- SPørre mot View'et i stede 
SELECT * 
FROM GodeKunder;

SELECT Fornavn,Etternavn,KNr,COUNT(*) AS AntallOrdre
FROM GodeKunder
WHERE KNr IN (SELECT KNr FROM Ordre)
GROUP BY Etternavn
HAVING AntallOrdre>=10;


-- Fra forelesning 8
SELECT KNr, COUNT(*) AS AntallBestillinger
FROM Ordre
GROUP BY KNr
HAVING AntallBestillinger>=10;

CREATE VIEW Gullklubben AS
(
SELECT;
)

SELECT *
FROM Gullklubben;

SELECT Gullklubben.KNr,Fornavn,Etternavn,Adresse,Kunde.Postnr,Poststed,AntallBestillinger
FROM Gullklubben,Kunde,Posted
WHERE Gullklubben.KNr=Kunde.KNr AND Kunde.Postnr=Poststed.Postnr;

CREATE VIEW GUllklbubblista AS
(
SELECT Gullklubbem.KNr,Fornavn,Etternavn,Adresse,Kunde.Postnr,Poststed,Antallbestillinger
FROM Gullklubben,Kunde,Poststed
WHERE Gullklubben.KNr=Kunde.KNR AND Kunde.Postnr=Poststed.Postnr
);

SELECT *
FROM Gullklubblista;

SELECT *
FROM Gullklubblista
ORDER BY AntallBestillinger DESC;

