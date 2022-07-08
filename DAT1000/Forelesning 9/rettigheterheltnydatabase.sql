USE nydatabase;

SELECT *
FROM VARE;

SELECT Betegnelse
FROM Vare;

-- UPDATE Vare
-- SET Antall='0'
-- WHERE VNr='13001';

-- CREATE USER 'Lagersjefen2022' IDENTIFIED BY 'lagerpw';

GRANT SELECT ON Vare TO 'Lagersjefen2022';


USE nydatabase;

GRANT INSERT ON Vare TO 'Lagersjefen2022';
GRANT UPDATE ON Vare TO 'Lagersjefen2022';
GRANT DELETE ON Vare TO 'Lagersjefen2022';
