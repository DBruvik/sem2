#Vindu ny vare forelesning 8 - 2022
#Vindu ny vare, forarbeid før forelesning 8


from ast import Delete
from tkinter import *
import mysql.connector

mindatabase=mysql.connector.connect(host='localhost',port=3306,
user='Lagersjefen2022',passwd='lagerpw',db='nydatabase')

window=Tk()
window.title("Nye varer")

settinnMarkor=mindatabase.cursor()
markor=mindatabase.cursor()

def leggTil():
    varenr=vnr.get()
    varenavn=vnavn.get()
    pris=vpris.get()
    katnr=vkatnr.get()
    antall=vantall.get()
    hylle=vhylle.get()

    settinnVare=("INSERT INTO Vare"
                "(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)"
                "VALUES(%s,%s,%s,%s,%s,%s)")
    datanyVare=(varenr,varenavn,pris,katnr,antall,hylle)

    settinnMarkor.execute(settinnVare,datanyVare)
    mindatabase.commit()
    lblLagret=Label(window,text='Varen er lagret!')
    lblLagret.grid(row=6,column=1,padx=5,pady=5,sticky=W)
    clearTekst()
    #4. Bruke Resultatet
    #for row in markor:
        #print(row)
    
    #markor.execute('SELECT * FROM Vare')
def clearTekst():
    entVnr.delete(0,'end')
    entVnavn.delete(0,'end')
    entVpris.delete(0,'end')
    entVkatnr.delete(0,'end')
    entVantall.delete(0,'end')
    entVhylle.delete(0,'end')

lblVarenr=Label(window,text='Oppgi varenr: ')
lblVarenr.grid(row=0,column=0,padx=5,pady=5,sticky=E)

lblVarenavn=Label(window,text='Oppgi varenavn: ')
lblVarenavn.grid(row=1,column=0,padx=5,pady=5,sticky=E)

lblPris=Label(window,text='Oppgi pris: ')
lblPris.grid(row=2,column=0,padx=5,pady=5,sticky=E)

lblKatnr=Label(window,text='Oppgi kategorinr: ')
lblKatnr.grid(row=3,column=0,padx=5,pady=5,sticky=E)

lblAntall=Label(window,text='Oppgi antall: ')
lblAntall.grid(row=4,column=0,padx=5,pady=5,sticky=E)

lblHylle=Label(window,text='Oppgi hylleplassering: ')
lblHylle.grid(row=5,column=0,padx=5,pady=5,sticky=E)

vnr=StringVar()
entVnr=Entry(window,width=6,textvariable=vnr)
entVnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

vnavn=StringVar()
entVnavn=Entry(window,width=20,textvariable=vnavn)
entVnavn.grid(row=1,column=1,padx=5,pady=5,sticky=W)

vpris=StringVar()
entVpris=Entry(window,width=5,textvariable=vpris)
entVpris.grid(row=2,column=1,padx=5,pady=5,sticky=W)

vkatnr=StringVar()
entVkatnr=Entry(window,width=4,textvariable=vkatnr)
entVkatnr.grid(row=3,column=1,padx=5,pady=5,sticky=W)

vantall=StringVar()
entVantall=Entry(window,width=4,textvariable=vantall)
entVantall.grid(row=4,column=1,padx=5,pady=5,sticky=W)

vhylle=StringVar()
entVhylle=Entry(window,width=4,textvariable=vhylle)
entVhylle.grid(row=5,column=1,padx=5,pady=5,sticky=W)

#Vi lager en knapp for å lagre ny vare
btnLagre=Button(window,text='Lagre',command=leggTil)
btnLagre.grid(row=6,column=2,padx=5,pady=5,sticky=W)

btnAvslutt=Button(window,text='Avslutt',command=window.destroy)
btnAvslutt.grid(row=8,column=2,padx=5,pady=5,sticky=W)

window.mainloop()
mindatabase.close()
