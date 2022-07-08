import mysql.connector
from tkinter import *
from tkinter import messagebox

#Program fra forelesning 8 oppgave 5
#Program med flere vinduer og flere funksjoner koblet opp imot database i mySQL


#Funksjon for scrollbar og lesing av lager ref oppgave 1 forelesning 8
def hentLager():
    def hentPrisoglager(event):
        valgt=lstVarer.get(lstVarer.curselection())
        #Finner riktig pris og varebeholdning, forutsetter at Betegnelse er unik
        #Bruker her for-løkke ofr gjennomgang av rader i prisoglagerMarkor,
        #Ville vært mer naturlig med en while-løkke struktur, leser nå alle rader hver gang
        #for row in prisoglagerMarkor:

        row=0
        funnet=False
        while funnet==False:
            if valgt==vareliste[row][0]:
                pris.set(vareliste[row][1])
                lager.set(vareliste[row][2])
                funnet=True
            row+=1
            
    #2. Oppretter cursor/markør
    vareMarkor=mindatabase.cursor()

    #3. Bruke databasen
    vareMarkor.execute('SELECT Betegnelse FROM Vare')

    #4 Bruke resultatet
    varer=[]
    for row in vareMarkor:
        varer+=[row[0]]
    

    vinduVarer=Toplevel()
    vinduVarer.title("Varer")

    yScroll=Scrollbar(vinduVarer,orient=VERTICAL)
    yScroll.grid(row=0,column=2,rowspan=10,padx=(0,100),pady=5,sticky=NS)

    innholdLstVarer=StringVar()
    lstVarer=Listbox(vinduVarer,width=50,height=10,listvariable=innholdLstVarer,yscrollcommand=yScroll.set)
    lstVarer.grid(row=0,column=1,rowspan=10,padx=(0,100),pady=5,sticky=E)
    innholdLstVarer.set(tuple(varer))
    yScroll["command"]=lstVarer.yview

    lblPris=Label(vinduVarer,text='Prisen er:')
    lblPris.grid(row=0,column=3,padx=5,pady=5,sticky=E)

    lblLager=Label(vinduVarer,text='Lagerstatusen er:')
    lblLager.grid(row=1,column=3,padx=5,pady=5,sticky=E)

    pris=StringVar()
    entPris=Entry(vinduVarer,width=10,state="readonly",textvariable=pris)
    entPris.grid(row=0,column=4,padx=5,pady=5,sticky=W)

    lager=StringVar()
    entLager=Entry(vinduVarer,width=10,state="readonly",textvariable=lager)
    entLager.grid(row=1,column=4,padx=5,pady=5,sticky=W)

    btnAvslutt=Button(vinduVarer,text='Tilbake til hovedmeny',command=vinduVarer.destroy)
    btnAvslutt.grid(row=7,column=3,columnspan=2,padx=5,pady=5,sticky=E)

    prisoglagerMarkor=mindatabase.cursor()
    prisoglagerMarkor.execute('SELECT Betegnelse,Pris,Antall FROM Vare')

    vareliste=[]
    for r in prisoglagerMarkor:
        vareliste+=[[r[0],r[1],r[2]]]


    lstVarer.bind("<<ListboxSelect>>",hentPrisoglager)
    print('Vis lager')
    prisoglagerMarkor.close()
    vareMarkor.close()

#Funksjon av registrering av vare ref oppgave 2 forelesning 8
def registrerVare():
    def leggTil():
        settinnMarkor=mindatabase.cursor()
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
        lblLagret=Label(vinduNyvare,text='Varen er lagret!')
        lblLagret.grid(row=6,column=1,padx=5,pady=5,sticky=W)
        clearTekst()
        settinnMarkor.close()

    def clearTekst():
        entVnr.delete(0,'end')
        entVnavn.delete(0,'end')
        entVpris.delete(0,'end')
        entVkatnr.delete(0,'end')
        entVantall.delete(0,'end')
        entVhylle.delete(0,'end') 

    vinduNyvare=Toplevel()
    vinduNyvare.title("Nye varer")    
    lblVarenr=Label(vinduNyvare,text='Oppgi varenr: ')
    lblVarenr.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    lblVarenavn=Label(vinduNyvare,text='Oppgi varenavn: ')
    lblVarenavn.grid(row=1,column=0,padx=5,pady=5,sticky=E)

    lblPris=Label(vinduNyvare,text='Oppgi pris: ')
    lblPris.grid(row=2,column=0,padx=5,pady=5,sticky=E)

    lblKatnr=Label(vinduNyvare,text='Oppgi kategorinr: ')
    lblKatnr.grid(row=3,column=0,padx=5,pady=5,sticky=E)

    lblAntall=Label(vinduNyvare,text='Oppgi antall: ')
    lblAntall.grid(row=4,column=0,padx=5,pady=5,sticky=E)

    lblHylle=Label(vinduNyvare,text='Oppgi hylleplassering: ')
    lblHylle.grid(row=5,column=0,padx=5,pady=5,sticky=E)

    vnr=StringVar()
    entVnr=Entry(vinduNyvare,width=6,textvariable=vnr)
    entVnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    vnavn=StringVar()
    entVnavn=Entry(vinduNyvare,width=20,textvariable=vnavn)
    entVnavn.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    vpris=StringVar()
    entVpris=Entry(vinduNyvare,width=5,textvariable=vpris)
    entVpris.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    vkatnr=StringVar()
    entVkatnr=Entry(vinduNyvare,width=4,textvariable=vkatnr)
    entVkatnr.grid(row=3,column=1,padx=5,pady=5,sticky=W)

    vantall=StringVar()
    entVantall=Entry(vinduNyvare,width=4,textvariable=vantall)
    entVantall.grid(row=4,column=1,padx=5,pady=5,sticky=W)

    vhylle=StringVar()
    entVhylle=Entry(vinduNyvare,width=4,textvariable=vhylle)
    entVhylle.grid(row=5,column=1,padx=5,pady=5,sticky=W)

    #Vi lager en knapp for å lagre ny vare
    btnLagre=Button(vinduNyvare,text='Lagre',command=leggTil)
    btnLagre.grid(row=6,column=2,padx=5,pady=5,sticky=W)

    btnAvslutt=Button(vinduNyvare,text='Tilbake til hovedmeny',command=vinduNyvare.destroy)
    btnAvslutt.grid(row=8,column=2,padx=5,pady=5,sticky=W)
    print('Registrer vare')

#Funksjon for oppdatering av lager ref oppgave 3 forelesning 8
def oppdaterLager():
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
        lblLagret=Label(vinduOppdater,text='          ')
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

        
        lblLagret=Label(vinduOppdater,text='Lagret')
        lblLagret.grid(row=5,column=1,columnspan=2,padx=5,pady=5,sticky=S)


    vinduOppdater=Toplevel()
    vinduOppdater.title("Oppdatere Varer")

    lblVarenr=Label(vinduOppdater,text='Oppgi varenr: ')
    lblVarenr.grid(row=0, column=0, padx=5, pady=5, sticky=E)
    lblVarenavn=Label(vinduOppdater, text='Varenavn: ')
    lblVarenavn.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    lblPris=Label(vinduOppdater, text='Pris: ')
    lblPris.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    lblKatnr=Label(vinduOppdater, text='Kategorinr: ')
    lblKatnr.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    lblAntall=Label(vinduOppdater,text='Antall: ')
    lblAntall.grid(row=4,column=0,padx=5,pady=5,sticky=E)
    lblOppdater=Label(vinduOppdater, text='Oppdater antall: ')
    lblOppdater.grid(row=5, column=0, padx=5, pady=5, sticky=E)
    lblHylle=Label(vinduOppdater, text='Hylleplassering: ')
    lblHylle.grid(row=6, column=0, padx=5, pady=5, sticky=E)

    vnr=StringVar()
    entVnr=Entry(vinduOppdater, width=6, textvariable=vnr)
    entVnr.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    vnavn=StringVar()
    entVnavn=Entry(vinduOppdater, state='readonly', width=20, textvariable=vnavn)
    entVnavn.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    vpris=StringVar()
    entVpris=Entry(vinduOppdater, state='readonly', width=5, textvariable=vpris)
    entVpris.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    vkatnr=StringVar()
    entVkatnr=Entry(vinduOppdater, state='readonly', width=4, textvariable=vkatnr)
    entVkatnr.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    vantallRead=StringVar()
    entVantall=Entry(vinduOppdater,state='readonly', width=4, textvariable=vantallRead)
    entVantall.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    vantall=StringVar()
    entVantall=Entry(vinduOppdater, width=4, textvariable=vantall)
    entVantall.grid(row=5, column=1, padx=5, pady=5, sticky=W)

    vhylle=StringVar()
    entVhylle=Entry(vinduOppdater, state='readonly', width=4, textvariable=vhylle)
    entVhylle.grid(row=6, column=1, padx=5, pady=5, sticky=W)

    btnSjekk=Button(vinduOppdater, text='Sjekk vare', command=hentLager)
    btnSjekk.grid(row=0, column=3, padx=5, pady=5, sticky=E)

    btnLagre=Button(vinduOppdater, text='Lagre', command=oppdater)
    btnLagre.grid(row=5, column=3, padx=5, pady=5, sticky=E)

    btnAvslutt=Button(vinduOppdater, text='Tilbake til hovedmeny', command=vinduOppdater.destroy)
    btnAvslutt.grid(row=6, column=3, padx=5, pady=5, sticky=E)
    print('Oppdater Lager')
def slettVare():
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
            messagebox.showinfo(message='Varen eksisterer ikke!')
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
        

    slettingVare=Toplevel()
    slettingVare.title("Slette Varer")

    lblVarenr=Label(slettingVare,text='Oppgi varenr: ')
    lblVarenr.grid(row=0, column=0, padx=5, pady=5, sticky=E)
    lblVarenavn=Label(slettingVare, text='Varenavn: ')
    lblVarenavn.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    lblPris=Label(slettingVare, text='Pris: ')
    lblPris.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    lblKatnr=Label(slettingVare, text='Kategorinr: ')
    lblKatnr.grid(row=3, column=0, padx=5, pady=5, sticky=E)
    lblAntall=Label(slettingVare,text='Antall: ')
    lblAntall.grid(row=4,column=0,padx=5,pady=5,sticky=E)
    lblHylle=Label(slettingVare, text='Hylleplassering: ')
    lblHylle.grid(row=5, column=0, padx=5, pady=5, sticky=E)

    vnr=StringVar()
    entVnr=Entry(slettingVare, width=6, textvariable=vnr)
    entVnr.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    vnavn=StringVar()
    entVnavn=Entry(slettingVare, state='readonly', width=20, textvariable=vnavn)
    entVnavn.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    vpris=StringVar()
    entVpris=Entry(slettingVare, state='readonly', width=5, textvariable=vpris)
    entVpris.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    vkatnr=StringVar()
    entVkatnr=Entry(slettingVare, state='readonly', width=4, textvariable=vkatnr)
    entVkatnr.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    vantall=StringVar()
    entVantall=Entry(slettingVare,state='readonly', width=4, textvariable=vantall)
    entVantall.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    vhylle=StringVar()
    entVhylle=Entry(slettingVare, state='readonly', width=4, textvariable=vhylle)
    entVhylle.grid(row=5, column=1, padx=5, pady=5, sticky=W)

    btnSjekk=Button(slettingVare, text='Sjekk vare', command=hentLager)
    btnSjekk.grid(row=0, column=3, padx=5, pady=5, sticky=E)

    btnSlett=Button(slettingVare,text='Slett vare',command=slettVareboks)
    btnSlett.grid(row=5,column=3,padx=5,pady=5,sticky=E)

    btnAvslutt=Button(slettingVare, text='Tilbake til hovedmeny', command=slettingVare.destroy)
    btnAvslutt.grid(row=6, column=3, padx=5, pady=5, sticky=E)
    print('Slett vare')


#1. Kobler mot databasen
mindatabase=mysql.connector.connect(host='localhost',port=3306,
user='Lagersjefen2022',passwd='lagerpw',db='nydatabase')

window=Tk()
window.title('Hele greia')

lblToptekst=Label(window,text='Program for uthenting av data i database')
lblToptekst.grid(row=0,column=0,padx=5,pady=5,sticky=W)

btnVare=Button(window,width=25,text='Vis varer',command=hentLager)
btnVare.grid(row=1,column=0,padx=5,pady=5,sticky=W)

btnRegistrer=Button(window,width=25,text='Registrer ny vare',command=registrerVare)
btnRegistrer.grid(row=2,column=0,padx=5,pady=5,sticky=W)

btnOppdater=Button(window,width=25,text='Oppdater varebeholdning',command=oppdaterLager)
btnOppdater.grid(row=3,column=0,padx=5,pady=5,sticky=W)

btnSlett=Button(window,width=25,text='Slett vare',command=slettVare)
btnSlett.grid(row=4,column=0,padx=5,pady=5,sticky=W)

btnAvslutt=Button(window,width=25,text='Avslutt program',fg="red",command=window.destroy)
btnAvslutt.grid(row=5,column=2,padx=5,pady=5,sticky=E)

window.mainloop()

#5. Koble ned databasen

mindatabase.close()