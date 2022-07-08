-- løsning av diverse oppgaver kap 2
-- oppgave 1
USE oppgave1kap2;

SELECT *
FROM Film;

-- g)
SELECT COUNT(*) AS IkkeTilSalgs
FROM Film
WHERE Pris IS NULL;
 
-- h)
SELECT COUNT(Pris) AS BilligFilmer
FROM Film
WHERE Pris<100;

-- i)
SELECT *
FROM Film
WHERE UCASE(Tittel) LIKE '%NOW';

-- oppgave 2
-- a)
SELECT Nr,Beskrivelse
FROM Hytte
WHERE Ukepris<4500
AND AntallSenger>=4;

-- e)
SELECT COUNT(*) AS AntallHytter
FROM Hytte
WHERE AvstandAlpin<500;

 
-- oppgave 3
USE hobbyhusetkap2;

SELECT *
FROM Vare;

-- 'gr og <blank> før stk.' er riktig skrivemåte
-- starter med å plukke ut de som har g som forkortelse for gram
-- alle "enheter" kommer etter et komma
SELECT *
FROM Vare
WHERE Betegnelse LIKE '%,%g';


-- Utfordringer med gruppering
USE gruppering2022;

SELECT *
FROM Ansatt;
 
-- En SELECT med en gruppering som er feil
SELECT Stillingskode,Lønnstrinn
FROM Ansatt
GROUP BY Stillingskode;

-- Riktig SELECT for setningen over er
SELECT Stillingskode,Lønnstrinn
FROM Ansatt
GROUP BY Stillingskode,Lønnstrinn;
 
-- Dersom vil vil finne antall ansatte i de ulike gruppene utvider vi setningen med en COUNT
SELECT Stillingskode,Lønnstrinn,COUNT(*) AS AntallAnsatte
FROM Ansatt
GROUP BY Stillingskode,Lønnstrinn;

-- Sammenlignet med å ha opptelling i SQL-setningen som er feil!!!!
SELECT Stillingskode,Lønnstrinn,COUNT(*) AS AntallAnsatte
FROM Ansatt
 GROUP BY Stillingskode;

-- Oppsummering
-- Gruppekriteriet: i SELECT-delen og GROUP BY
-- Gruppebetingelse: HAVING
-- COUNT(*) vs COUNT(kolonnenavn)
-- "sammensatt gruppekriterie": for å unngå meningsløse spørringer/spørreresultater er det et krav i SQL 
-- at enhver kolonne som forekommer i SELECT-delen også er med i GROUP BY
-- Det er ikke tillatt å bruke mengdefunksjoner i WHERE-betingelsen