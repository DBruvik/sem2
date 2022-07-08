USE oppgave1kap2;

SELECT *
FROM film;

SELECT Tittel
FROM film
WHERE Land='USA' AND (År BETWEEN 1980 AND 1989);

SELECT *
FROM film
WHERE Sjanger='Komedie' AND (Alder<10) AND (Tid<130);

SELECT Tittel
FROM film
WHERE Sjanger='Western' OR Sjanger='Action';

SELECT DISTINCT Land
FROM film
ORDER BY Land;

SELECT Tittel
FROM film
WHERE Tittel LIKE '%now';

-- Nye oppgaver

-- g)
SELECT COUNT(*) AS AntallFilmer
FROM film
WHERE Pris IS NULL;
-- h)
SELECT COUNT(pris) AS PrisUnder100
FROM film
WHERE Pris<100;
-- i)
SELECT Tittel
FROM film
WHERE UCASE(Tittel) LIKE '%NOW';

