use ansattpersonal2022;

-- Data i tabellen Ansatt
SELECT *
FROM ansatt;

-- Data i tabellen Postkatalog
SELECT *
FROM Postkatalog;

-- Kryssproduktet av Postkatalog og Ansatt
SELECT *
FROM Postkatalog, Ansatt;

-- Likekobling, liste over ansatte med postadresse, med WHERE-betingelser
SELECT *
FROM Ansatt, Postkatalog
WHERE Ansatt.Postnr=Postkatalog.Postnr;

-- Med kolonnevalg
SELECT Ansattnr, Fornavn, Etternavn, Gateadresse, Ansatt.Postnr, Poststed
FROM Ansatt, Postkatalog
WHERE Ansatt.Postnr=Postkatalog.Postnr;

-- Likekobling, liste over ansatte med postadresser, med INNER JOIN
SELECT Ansattnr, Fornavn, Etternavn, Gateadresse, Ansatt.Postnr, Poststed
FROM Ansatt INNER JOIN Postkatalog
	ON Ansatt.Postnr=Postkatalog.Postnr;

-- Likekobling 3 tabeller, liste over ansatte med stilling og avdeling, med WHERE-betingelser
SELECT Etternavn, Fornavn, Stillingsbetegnelse, Avdelingsnavn
FROM Ansatt, Stillingstype, Avdeling
WHERE Ansatt.Stillingskode=Stillingstype.Stillingskode
	AND Ansatt.Avdelingsnr=Avdeling.Avdelingsnr;

-- Koble tre eller flere tabeller, først 2, "steg for steg" tankegang
SELECT Etternavn, Fornavn, Stillingsbetegnelse
-- Avdelingsnavn her
FROM Ansatt, Stillingstype
-- , avdeling
WHERE Ansatt.Stillingskode=Stillingstype.Stillingskode
-- AND Ansatt.Avdelingsnr=Avdeling.Avdelingsnr
;

-- ved bruk av INNER JOIN kan det være enda viktigere å bygge opp "steg for steg"
-- Først Ansatt mot avdeling(innerste JOIN) før
-- Stillingstype kobles opp mot mellomresultatet av innerste JOIN

SELECT Etternavn, Fornavn, Stillingsbetegnelse, Avdelingsnavn
FROM Stillingstype INNER JOIN
	(Ansatt INNER JOIN Avdeling
		ON Ansatt.Avdelingsnr=Avdeling.Avdelingsnr)
	ON Stillingstype.Stillingskode=Ansatt.Stillingskode;
    
-- Alternativ med INNER JOIN
-- Først Ansatt mot Stillingstype (innerste JOIN) førelease savepoint
-- Avdeling kobles mot mellomresultat av innerste JOIN
SELECT Etternavn, Fornavn, Stillingsbetegnelse, Avdelingsnavn
FROM Avdeling INNER JOIN
	(Ansatt INNER JOIN Stillingstype
		ON Ansatt.Stillingskode=Stillingstype.Stillingskode)
	ON Avdeling.Avdelingsnr=Ansatt.Avdelingsnr;
    
-- View/utsnitt
-- Oppretting av view Ansattliste
-- Etternavn, Fornavn, Stilling, Avdeling med info fra de 3 tabellene
-- Ansatt, Stillingstype, Avdeling 
DROP VIEW IF EXISTS Ansattliste;

CREATE VIEW Ansattliste (Etternavn, Fornavn, Stilling, Avdeling) AS
(SELECT Etternavn, Fornavn, Stillingsbetegnelse, Avdelingsnavn
FROM Ansatt, Stillingstype, Avdeling
WHERE Ansatt.Stillingskode=Stillingstype.Stillingskode
	AND Ansatt.Avdelingsnr=Avdeling.Avdelingsnr);


-- Kan så kjøringer mot view'et
SELECT * 
FROM Ansattliste
ORDER BY Etternavn;

-- Ytre koblinger
-- Ønsker også stillingsbetegnelser som ikke er i bruk (ingen har PT)
SELECT *
FROM Stillingstype LEFT OUTER JOIN Ansatt
	on Stillingstype.Stillingskode=Ansatt.Stillingskode;

-- Ekvivalet med (samme spørreresultat, annen presentasjon)
SELECT *
FROM Ansatt RIGHT OUTER JOIN Stillingstype
	ON Ansatt.Stillingskode=Stillingstype.Stillingskode;

-- Ønsker også avdelinger som ingen er tilknytta pt
SELECT *
From Avdeling LEFT OUTER JOIN Ansatt
		ON Avdeling.Avdelingsnr=Ansatt.Avdelingsnr;

-- Ekvivalent med (samme spørreresultat, annen presentasjon)
SELECT *
FROM Ansatt RIGHT OUTER JOIN Avdeling
	ON Ansatt.Avdelingsnr=Avdeling.Avdelingsnr;
    