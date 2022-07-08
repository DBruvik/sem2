USE hobbyhusetkap2;

SELECT *
FROM Vare;

SELECT *
FROM Vare
WHERE (pris<100) AND ((Kategori='Bøker') OR (Kategori='Keramikk'));

SELECT VNr,Betegnelse,Pris, ROUND(Pris*1.25,2) AS PrisInklMva
FROM Vare;

SELECT VNr, Betegnelse, LEFT(Hylle,1) AS Hylleseksjon
FROM Vare;

SELECT *
FROM Vare
WHERE (pris>=57) AND (pris<=75.50);

SELECT *
FROM Vare
WHERE pris BETWEEN 57 AND 75.50;

SELECT *
FROM Vare
WHERE Betegnelse LIKE 'M%';

SELECT *
FROM Vare
WHERE UPPER (LEFT(Betegnelse,1))='M';

SELECT *
FROM Vare
WHERE UPPER(Betegnelse) LIKE '%MARSIPAN%';

SELECT *
FROM Vare
ORDER BY Kategori ASC, Pris DESC;

SELECT ROUND(AVG(Pris),2) AS Gjennomsnittspris
FROM Vare
WHERE Kategori='Fiske';

SELECT COUNT(*) AS AntallBlomsterVarer
FROM Vare
WHERE Kategori='Blomsterfrø' OR Kategori='Blomsterløker';
-- Annen måte å løse dette på
SELECT SUM(Antall) 
FROM Vare
WHERE Kategori='Blomsterfrø' OR Kategori='Blomsterløker';

SELECT Kategori, COUNT(*) AS Antall
FROM Vare
GROUP BY Kategori
HAVING Antall>1;

-- Annen måte og løse det på
SELECT Kategori, COUNT(*) AS Antall
FROM Vare
GROUP BY Kategori
HAVING COUNT(*) >1;


-- Oppgave 3
SELECT *
FROM Vare
WHERE (UPPER(Betegnelse) LIKE '%,%' AND UPPER(Betegnelse) LIKE '%stk');

SELECT *
FROM Vare
WHERE (UPPER(Betegnelse) LIKE '%g' or  UPPER(Betegnelse) LIKE '%gr') AND (Betegnelse) LIKE'%,%';