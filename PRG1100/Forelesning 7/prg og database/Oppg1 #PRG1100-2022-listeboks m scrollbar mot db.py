#PRG1100-2022-listeboks m scrollbar mot db

import mysql.connector
from tkinter import *

def hentPrisoglager(event):
    valgt=lstVarer.get(lstVarer.curselection())
   

    #Finner riktig pris og varebeholdning, forutsetter at Betegnelse er unik
    #Bruker her for-løkke ofr gjennomgang av rader i prisoglagerMarkor,
    #Ville vært mer naturlig med en while-løkke struktur, leser nå alle rader hver gang
    #for row in prisoglagerMarkor:
    row=0
    tall=0
    funnet=False
    while not funnet:
        tall+=1
        if valgt==vareliste[row][0]:
            pris.set(vareliste[row][1])
            lager.set(vareliste[row][2])
            funnet=True
        row=+1
            


#1. Kobler mot databasen
mindatabase=mysql.connector.connect(host='localhost',port=3306,
user='Lagersjefen2022',passwd='lagerpw',db='nydatabase')

#2. Oppretter cursor/markør
vareMarkor=mindatabase.cursor()

#3. Bruke databasen
vareMarkor.execute('SELECT Betegnelse FROM Vare')

#4 Bruke resultatet
varer=[]
for row in vareMarkor:
    varer+=row


window=Tk()
window.title("Varer")

yScroll=Scrollbar(window,orient=VERTICAL)
yScroll.grid(row=0,column=2,rowspan=10,padx=(0,100),pady=5,sticky=NS)

innholdLstVarer=StringVar()
lstVarer=Listbox(window,width=50,height=10,listvariable=innholdLstVarer,yscrollcommand=yScroll.set)
lstVarer.grid(row=0,column=1,rowspan=10,padx=(0,100),pady=5,sticky=E)
innholdLstVarer.set(tuple(varer))
yScroll["command"]=lstVarer.yview

lblPris=Label(window,text='Prisen er:')
lblPris.grid(row=0,column=3,padx=5,pady=5,sticky=E)

lblLager=Label(window,text='Lagerstatusen er:')
lblLager.grid(row=1,column=3,padx=5,pady=5,sticky=E)

pris=StringVar()
entPris=Entry(window,width=10,state="readonly",textvariable=pris)
entPris.grid(row=0,column=4,padx=5,pady=5,sticky=W)

lager=StringVar()
entLager=Entry(window,width=10,state="readonly",textvariable=lager)
entLager.grid(row=1,column=4,padx=5,pady=5,sticky=W)


prisoglagerMarkor=mindatabase.cursor()
prisoglagerMarkor.execute('SELECT Betegnelse,Pris,Antall FROM Vare')

vareliste=[]
for r in prisoglagerMarkor:
    vareliste+=[[r[0],r[1],r[2]]]


lstVarer.bind("<<ListboxSelect>>",hentPrisoglager)

window.mainloop()

#5. Koble ned databasen
prisoglagerMarkor.close()
vareMarkor.close()
mindatabase.close()
