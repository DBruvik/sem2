#PRG1100-2022-listeboks m scrollbar mot db
from logging.config import listen
import mysql.connector
from tkinter import *

def hentLager():
    alleVarerMarkor=mindatabase.cursor()
    alleVarerMarkor.execute('SELECT * FROM Vare')

    vareliste=[]
    for row in alleVarerMarkor:
        vareliste+=[[row[0],row[1],row[2],row[3],row[4],row[5]]]
    
    alleVarerMarkor.close()

    valgt=vnr.get()
    rad=0
    funnet=False
    while funnet==False:
        if valgt==vareliste[rad][0]:
            vnavn.set(vareliste[rad][1])
            vpris.set(vareliste[rad][2])
            vkatnr.set(vareliste[rad][3])
            vantallRead.set(vareliste[rad][4])
            vantall.set(vareliste[rad][4])
            if vareliste[rad][5]==None:
                vhylle.set('NULL')
            else:
                vhylle.set(vareliste[rad][5])
            funnet=True
        rad+=1
    lblLagret=Label(window,text='          ')
    lblLagret.grid(row=5,column=1,columnspan=2,padx=5,pady=5,sticky=S)
    entVantall.delete(0,'end')
    

def oppdater():

    oppdateringMarkor=mindatabase.cursor()
    oppdaterAntall=('''UPDATE Vare
                    SET Antall=0, Antall=%s
                    WHERE VNr=%s''')
    antall=vantall.get()
    varenummer=vnr.get()
    oppdaterAntallVarer=(antall,varenummer)

    oppdateringMarkor.execute(oppdaterAntall,oppdaterAntallVarer)
    mindatabase.commit()
    oppdateringMarkor.close()

    
    lblLagret=Label(window,text='Lagret')
    lblLagret.grid(row=5,column=1,columnspan=2,padx=5,pady=5,sticky=S)



#1. Kobler mot databasen
mindatabase=mysql.connector.connect(host='localhost',port=3306,
user='Lagersjefen2022',passwd='lagerpw',db='nydatabase')



window=Tk()
window.title("Oppdatere Varer")

lblVarenr=Label(window,text='Oppgi varenr: ')
lblVarenr.grid(row=0, column=0, padx=5, pady=5, sticky=E)
lblVarenavn=Label(window, text='Varenavn: ')
lblVarenavn.grid(row=1, column=0, padx=5, pady=5, sticky=E)
lblPris=Label(window, text='Pris: ')
lblPris.grid(row=2, column=0, padx=5, pady=5, sticky=E)
lblKatnr=Label(window, text='Kategorinr: ')
lblKatnr.grid(row=3, column=0, padx=5, pady=5, sticky=E)
lblAntall=Label(window,text='Antall: ')
lblAntall.grid(row=4,column=0,padx=5,pady=5,sticky=E)
lblOppdater=Label(window, text='Oppdater antall: ')
lblOppdater.grid(row=5, column=0, padx=5, pady=5, sticky=E)
lblHylle=Label(window, text='Hylleplassering: ')
lblHylle.grid(row=6, column=0, padx=5, pady=5, sticky=E)

vnr=StringVar()
entVnr=Entry(window, width=6, textvariable=vnr)
entVnr.grid(row=0, column=1, padx=5, pady=5, sticky=W)

vnavn=StringVar()
entVnavn=Entry(window, state='readonly', width=20, textvariable=vnavn)
entVnavn.grid(row=1, column=1, padx=5, pady=5, sticky=W)

vpris=StringVar()
entVpris=Entry(window, state='readonly', width=5, textvariable=vpris)
entVpris.grid(row=2, column=1, padx=5, pady=5, sticky=W)

vkatnr=StringVar()
entVkatnr=Entry(window, state='readonly', width=4, textvariable=vkatnr)
entVkatnr.grid(row=3, column=1, padx=5, pady=5, sticky=W)

vantallRead=StringVar()
entVantall=Entry(window,state='readonly', width=4, textvariable=vantallRead)
entVantall.grid(row=4, column=1, padx=5, pady=5, sticky=W)

vantall=StringVar()
entVantall=Entry(window, width=4, textvariable=vantall)
entVantall.grid(row=5, column=1, padx=5, pady=5, sticky=W)

vhylle=StringVar()
entVhylle=Entry(window, state='readonly', width=4, textvariable=vhylle)
entVhylle.grid(row=6, column=1, padx=5, pady=5, sticky=W)

btnSjekk=Button(window, text='Sjekk vare', command=hentLager)
btnSjekk.grid(row=0, column=3, padx=5, pady=5, sticky=E)

btnLagre=Button(window, text='Lagre', command=oppdater)
btnLagre.grid(row=5, column=3, padx=5, pady=5, sticky=E)

btnAvslutt=Button(window, text='Avslutt', command=window.destroy)
btnAvslutt.grid(row=6, column=3, padx=5, pady=5, sticky=E)

window.mainloop()

#5. Koble ned databasen

mindatabase.close()
