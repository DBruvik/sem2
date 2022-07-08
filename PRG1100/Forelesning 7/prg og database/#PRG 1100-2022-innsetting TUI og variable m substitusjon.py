#PRG 1100-2022-innsetting TUI og variable m substitusjon

#Innsetting av data i database fra Python
#Innsetting ved verdiene inn i variable som referes i cursoren

import mysql.connector

#1. Kobler mot databasen
mindatabase=mysql.connector.connect(host='localhost', port=3306,
user='Lagersjefen2022',passwd='lagerpw',db='nydatabase')

#2. Oppretter cursoren/markøren
settinnMarkor=mindatabase.cursor()
markor=mindatabase.cursor()

#3. Bruker databasen
varenr=input('Oppgi varenr: ')
varenavn=input('Oppgi varenavn: ')
pris=float(input('Oppgi pris: '))
katnr=int(input('Oppgi kategorinr: '))
antall=int(input('Oppgi antall: '))
hylle=input('Oppgi hylleplassering: ')

settinnMarkor.execute("INSERT INTO Vare"
                     "(VNR,Betegnelse,Pris,KatNr,Antall,Hylle)"
                     "VALUES('9999','testvare',99.99,999,99,'T99')")
mindatabase.commit()
settinnVare=("INSERT INTO Vare"
             "(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)"
             "VALUES(%s,%s,%s,%s,%s,%s)")
datanyVare=(varenr,varenavn,pris,katnr,antall,hylle)

settinnMarkor.execute(settinnVare,datanyVare)
mindatabase.commit()

markor.execute('SELECT * FROM Vare')

#4. Bruke Resultatet
for row in markor:
    print(row)

#5. Koble ned databasen
settinnMarkor.close()
markor.close()

mindatabase.close()
    
