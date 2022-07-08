#PRG1100-2022-listeboks m scrollbar mot db
import mysql.connector
from tkinter import *
from tkinter import messagebox

def hentLager():
    try:
        alleVarerMarkor=mindatabase.cursor()
        alleVarerMarkor.execute('SELECT * FROM Vare')

        vareliste=[]
        for row in alleVarerMarkor:
            vareliste+=[[row[0],row[1],row[2],row[3],row[4],row[5]]]
        
        alleVarerMarkor.close()

        valgt=vnr.get()
        print(valgt)
        rad=0
        funnet=False
        while funnet==False:
            if valgt==vareliste[rad][0]:
                vnavn.set(vareliste[rad][1])
                vpris.set(vareliste[rad][2])
                vkatnr.set(vareliste[rad][3])
                vantall.set(vareliste[rad][4])
                if vareliste[rad][5]==None:
                    vhylle.set('NULL')
                else:
                    vhylle.set(vareliste[rad][5])
                funnet=True
            rad+=1
    except IndexError:
        lblEksistererikke=Label(window,text='Varen eksisterer ikke!')
        lblEksistererikke.grid(row=6,column=2,padx=5,pady=5,sticky=W)
  

def sletting():

    varenummer=vnr.get()
    slettingMarkor=mindatabase.cursor()
    slettVare=('''DELETE FROM Vare WHERE VNr=%s''')
    slettingMarkor.execute(slettVare,(varenummer,))
    mindatabase.commit()
    slettingMarkor.close()

    messagebox.showinfo(message='Vare er slettet')

def slettVareboks():
    slettVindu=Toplevel()
    slettVindu.title('Sletting Popup')

    lblOverskrift=Label(slettVindu,text='Vil du slette valgt vare?')
    lblOverskrift.grid(row=0,column=0,padx=5,pady=5,sticky=N)

    btnJa=Button(slettVindu,text='Ja',command=sletting)
    btnJa.grid(row=2,column=0,pady=5,padx=5,sticky=W)

    btnNei=Button(slettVindu,text='Nei',command=slettVindu.destroy)
    btnNei.grid(row=2,column=3,pady=5,padx=5,sticky=E)

    btnHoved=Button(slettVindu,text='Tilbake',command=slettVindu.destroy)
    btnHoved.grid(row=3,column=3,pady=5,padx=5,sticky=E)
    

#1. Kobler mot databasen
mindatabase=mysql.connector.connect(host='localhost',port=3306,
user='Lagersjefen2022',passwd='lagerpw',db='nydatabase')

window=Tk()
window.title("Slette Varer")

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
lblHylle=Label(window, text='Hylleplassering: ')
lblHylle.grid(row=5, column=0, padx=5, pady=5, sticky=E)

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

vantall=StringVar()
entVantall=Entry(window,state='readonly', width=4, textvariable=vantall)
entVantall.grid(row=4, column=1, padx=5, pady=5, sticky=W)

vhylle=StringVar()
entVhylle=Entry(window, state='readonly', width=4, textvariable=vhylle)
entVhylle.grid(row=5, column=1, padx=5, pady=5, sticky=W)

btnSjekk=Button(window, text='Sjekk vare', command=hentLager)
btnSjekk.grid(row=0, column=3, padx=5, pady=5, sticky=E)

btnSlett=Button(window,text='Slett vare',command=slettVareboks)
btnSlett.grid(row=5,column=3,padx=5,pady=5,sticky=E)

btnAvslutt=Button(window, text='Avslutt', command=window.destroy)
btnAvslutt.grid(row=6, column=3, padx=5, pady=5, sticky=E)
window.mainloop()

#5. Koble ned databasen

mindatabase.close()
