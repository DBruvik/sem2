USE ??????

-- a)
SELECT Nr, Beskrivelse
FROM Hytte
WHERE (Ukepris<4500) AND (AntallSenger>=4);

-- b)
SELECT *
FROM Hytte
WHERE Strøm LIKE 'J%' OR Dusj LIKE 'J%'
ORDER BY Ukepris ASC;

-- c)
SELECT AntallSenger, COUNT(*) AS Sengeplasser
FROM Hytte
GROUP BY AntallSenger
HAVING Sengeplasser>1;

-- d)
SELECT ROUND(AVG(Ukepris),2) AS Gjennomsnittspris
FROM Hytte
WHERE AntallSenger=4;

-- e)
SELECT COUNT(*) AS Antall
FROM Hytte
WHERE AvstandAlpin<500;

-- Ståle sin løsning
-- a)
SELECT Nr,Beskrivelse
FROM Hytte
WHERE Ukepris<4500 AND AntallSenger>=4;

-- e)
SELECT COUNT(*) AS AntallHytter
FROM Hytte
WHERE AvstandAlpin<500;
    