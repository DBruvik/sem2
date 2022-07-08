USE gruppering2022;

SELECT *
FROM Ansatt;

SELECT Stillingskode
FROM Ansatt;

SELECT *
FROM Ansatt
GROUP BY Lønnstrinn;

SELECT Stillingskode, COUNT(*) AS AntStillingskoder
FROM Ansatt
GROUP BY Stillingskode;

-- Sammenlignet med å ha opptelling i SQL-setningen som er feil
SELECT Stillingskode,Lønnstrinn,COUNT(*) AS AntallAnsatte
FROM Ansatt
GROUP BY Stillingskode;

-- RIKTIG SELECT
SELECT Stillingskode, Lønnstrinn
FROM Ansatt
GROUP BY Stillingskode,Lønnstrinn;