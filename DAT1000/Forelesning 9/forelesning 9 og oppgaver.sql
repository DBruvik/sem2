USE Hobbyhuset;

CREATE VIEW Bestilling (VNr,Navn,Hylle,Pris) AS
(
SELECT VNr, Betegnelse,Hylle,Pris
FROM VARE
WHERE ANtall<5
);

SELECT VNr,Navn
FROM Bestilling
WHERE Pris>100
ORDER BY Navn;

SELECT VNr,Betegnelse AS Navn
FROM Vare
WHERE Antall<5 AND Pris>100
ORDER BY Navn;

DROP VIEW IF EXISTS AntallVarerPrKategori;
CREATE VIEW AntallVarerPrKategori AS
(
SELECT KatNr,COUNT(*) AS Antall
FROM Vare
GROUP BY KatNr
);

SELECT *
FROM AntallVarerPrKategori
WHERE Antall>5;


SELECT KatNr, COUNT(*) AS Antall
FROM VARE
GROUP BY KatNr
HAVING Antall>5;

-- A)
SELECT *
FROM Vare,KatNr;

-- B)
SELECT *
FROM Vare, Kategori
WHERE Vare.KatNr=Kategori.KatNr;

-- C)
SELECT Ordrelinje.OrdreNr,Vare.VNr,Ordrelinje.PrisPrEnhet,Ordrelinje.Antall,Vare.Betegnelse,Ordre.OrdreDato
FROM Ordrelinje,Vare,Ordre
WHERE Ordrelinje.OrdreNr=Ordre.OrdreNr AND Ordrelinje.VNr=Vare.VNr; 

-- Fastit C)
SELECT Ordrelinje.*,Vare.Betegnelse,Ordre.OrdreDato
FROM Ordrelinje,Ordre,Vare
WHERE Ordrelinje.OrdreNr=Ordre.OrdreNr AND Ordrelinje.VNr=Vare.VNr;


-- D)
SELECT Ordrelinje.OrdreNr,Vare.VNr,Ordrelinje.PrisPrEnhet,Ordrelinje.Antall,Vare.Betegnelse,Ordre.Ordredato, ((PrisPrEnhet)*(Ordrelinje.Antall)) AS Totalbeløp
FROM Ordrelinje,Vare,Ordre
WHERE Ordrelinje.OrdreNr=Ordre.OrdreNr AND Ordrelinje.VNr=Vare.VNr
GROUP BY Ordrelinje.OrdreNr,Vare.VNr,Ordrelinje.PrisPrEnhet,Ordrelinje.Antall,Vare.Betegnelse,Ordre.Ordredato;

-- Fasit D)
SELECT OL.*,V.Betegnelse,O.OrdreDato,OL.Antall*OL.PrisPrEnhet AS Beløp
FROM Ordrelinje AS OL, Ordre AS O, Vare AS V
WHERE OL.OrdreNr=O.OrdreNr AND OL.VNr=V.VNr;
-- E)
SELECT OL.Antall*OL.PrisPrEnhet*COUNT(O.KNr) AS Beløp, O.KNr AS KNr, COUNT(O.KNr) AS AntallOrdre
FROM Ordrelinje AS OL, Ordre AS O, Vare AS V
WHERE OL.OrdreNr=O.OrdreNr AND OL.VNr=V.VNr
GROUP BY KNr;

-- FASIT E)
SELECT K.KNr, K.Fornavn,K.Etternavn,
SUM(OL.Antall*OL.PrisPrEnhet) AS Beløp
FROM Ordrelinje AS OL, Ordre AS O, Kunde AS K
WHERE OL.OrdreNr=O.OrdreNr AND K.KNr=O.KNr
GROUP BY K.KNr, K.Fornavn,K.Etternavn;

SELECT *
FROM Ordre
GROUP BY KNr;

SELECT *
FROM Ordrelinje;
