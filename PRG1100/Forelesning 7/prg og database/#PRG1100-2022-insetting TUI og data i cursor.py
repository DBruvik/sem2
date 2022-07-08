#PRG1100-2022-insetting TUI og data i cursor
#Innsetting av data i database fra Python
#Innsetting ved verdiene "rett i cursoren"

import mysql.connector

#1. Kobler mot databasen
mindatabase=mysql.connector.connect(host='localhost',port=3306,
user='Lagersjefen2022',passwd='lagerpw',db='nydatabase')

#2. Oppretter cursoren/markøren
settinnMarkor=mindatabase.cursor()
markor=mindatabase.cursor()

#3 Bruke databasen
settinnMarkor.execute("INSERT INTO Vare"
                      "(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)"
                      "VALUES('2222','Testvare',99.99,999,99,'T99')")
mindatabase.commit()
settinnMarkor.execute("INSERT INTO Vare"
                     "(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)"
                     "VALUES('8888','Endaentestvare',88.88,888,88,'T88')")
mindatabase.commit()

markor.execute('SELECT * FROM Vare')

#4. Bruke resultate
for row in markor:
    print(row)

#5. Koble ned databasen
settinnMarkor.close()
markor.close()

mindatabase.close()
