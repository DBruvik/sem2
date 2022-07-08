USE ansattpersonal2022;

INSERT INTO Stillingstype(Stillingskode,Stillingsbetegnelse) VALUES('1000','Avdelingssjef');
INSERT INTO Stillingstype(Stillingskode,Stillingsbetegnelse) VALUES('2000','Konsulent');
INSERT INTO Stillingstype(Stillingskode,Stillingsbetegnelse) VALUES('3000','Økonomi medarbeider');
INSERT INTO Stillingstype(Stillingskode,Stillingsbetegnelse) VALUES('4000','Sekretær');
INSERT INTO Stillingstype(Stillingskode,Stillingsbetegnelse) VALUES('5000','Trainee');

INSERT INTO Avdeling(Avdelingsnr,Avdelingsnavn) VALUES('1000','IT');
INSERT INTO Avdeling(Avdelingsnr,Avdelingsnavn) VALUES('2000','Administrasjon');
INSERT INTO Avdeling(Avdelingsnr,Avdelingsnavn) VALUES('3000','Økonomi');
INSERT INTO Avdeling(Avdelingsnr,Avdelingsnavn) VALUES('4000','Personal');
INSERT INTO Avdeling(Avdelingsnr,Avdelingsnavn) VALUES('5000','Vedlikehold');

INSERT INTO Kurs(Kursnr,Kursnavn) VALUES('1000','HMS');
INSERT INTO Kurs(Kursnr,Kursnavn) VALUES('2000','Brannvakt');
INSERT INTO Kurs(Kursnr,Kursnavn) VALUES('3000','Førstehjelp');
INSERT INTO Kurs(Kursnr,Kursnavn) VALUES('4000','Sistehjelp');

INSERT INTO Postkatalog(Postnr,Poststed) VALUES('1000','Storeby');
INSERT INTO Postkatalog(Postnr,Poststed) VALUES('1500','Lilleby');
INSERT INTO Postkatalog(Postnr,Poststed) VALUES('2000','Mellomby');
INSERT INTO Postkatalog(Postnr,Poststed) VALUES('2500','Storebygd');
INSERT INTO Postkatalog(Postnr,Poststed) VALUES('3000','Melommbygd');
INSERT INTO Postkatalog(Postnr,Poststed) VALUES('3500','Lillebygd');

INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,telefonnr,Stillingskode,Avdelingsnr,Postnr) VALUES('1000','Ole','Olsen','Olsengate 1','11111111','1000','3000','2000');
INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,telefonnr,Stillingskode,Avdelingsnr,Postnr) VALUES('2000','Hans','Hansen','Hansengate 2','22222222','4000','5000','3500');
INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,telefonnr,Stillingskode,Avdelingsnr,Postnr) VALUES('3000','Jens','Jensen','Jensengate 3','33333333','2000','4000','1000');
INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,telefonnr,Stillingskode,Avdelingsnr,Postnr) VALUES('4000','Trine','Trinesen','Trinesengate 4','44444444','3000','1000','1500');
INSERT INTO Ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,telefonnr,Stillingskode,Avdelingsnr,Postnr) VALUES('5000','Kari','Karisen','Karisengate 5','55555555','5000','2000','3000');

INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('1000','1000','2022.02.03','Godkjent');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('1000','2000','2021.10.15','Ikke Godkjent');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('2000','1000','2020.08.20','Godkjent');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('2000','2000','2018.12.01','Ikke Godkjent');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('3000','3000','2022.01.10','Godkjent');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('4000','2000','2010.05.16','Ikke Godkjent');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('5000','2000','2022.06.17','Godkjent');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('5000','3000','2015.08.24','Ikke Godkjent');
