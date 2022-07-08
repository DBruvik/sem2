USE Hotelldatabase;

SELECT *
FROM Bestilling;


SELECT Rom.Romnr
FROM ROM
LEFT OUTER JOIN Bestilling ON Rom.Romnr=Bestilling.Romnr
WHERE Rom.Romnr IN (SELECT Romnr
					FROM Bestilling
                    WHERE Tildato=20220104 OR Fradato=20220111)
OR Rom.Romnr NOT IN (SELECT Romnr
						FROM Bestilling
						WHERE (Fradato<=20220104 AND Tildato>=20220111)
                        OR ((Fradato BETWEEN 20220104 AND 20220111)
                        OR (Tildato BETWEEN 20220104 AND 20220111)))
GROUP BY Rom.Romnr;