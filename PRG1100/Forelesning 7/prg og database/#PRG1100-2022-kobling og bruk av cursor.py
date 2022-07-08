import mysql.connector
#PRG1100-2022-kobling og bruk av cursor


#1. Kobler mot databasen
mindatabase=mysql.connector.connect(host='localhost',port=3306,
user='Lagersjefen2022',passwd='lagerpw',db='heltnydatabase')

#2. Oppretter cursoren/markøren
markor=mindatabase.cursor()

#3. Bruke databasen
markor.execute("SELECT * FROM Vare")

#4. Bruke resultate
for row in markor:
    print(row)

#5.Koble ned databasen, cursoren stenges etter bruk, koblingen stenges ved programslutt
markor.close()

mindatabase.close()