-- spørring mot systemtabeller
USE INFORMATION_SCHEMA;
 
-- Denne spørringen gir oversikt over alle tabeller
-- for alle databasene
SELECT *
FROM TABLES;
   
-- Denne gir oversikt over alle systemtabellene 
-- du kan spørre mot
SELECT *
FROM TABLES
WHERE TABLE_SCHEMA='information_schema';
   
   
SELECT *
FROM TABLES
WHERE TABLE_SCHEMA='Ansattpersonal2022';
   
SELECT *
FROM COLUMNS
WHERE TABLE_NAME='Kursdeltagelse';
   
SELECT *
FROM TABLE_CONSTRAINTS
WHERE TABLE_SCHEMA='Ansattpersonal2022';
   
SELECT *
FROM REFERENTIAL_CONSTRAINTS;
   
SELECT *
FROM VIEWS;
   
SELECT *
FROM USER_PRIVILEGES;
   
SELECT *
FROM STATISTICS;
   
-- Sekvens med spørringer for å se indekstype for ny indeks
-- 1)
-- Se hvilke indekser som har blitt opprettet
-- og indekstype B-tre
SELECT *
FROM STATISTICS
WHERE TABLE_SCHEMA='Hobbyhuset';
   
-- 2)
USE Hobbyhuset;
CREATE INDEX EtternavnIDX ON Kunde(Etternavn);
   
-- 3)
USE INFORMATION_SCHEMA;
   
SELECT *
FROM STATISTICS
WHERE TABLE_SCHEMA='Hobbyhuset';