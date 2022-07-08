import mysql.connector
from tkinter import *

def hent_vare(): 
     
    valgt=vnr.get()
    funnet=False
    rad=0     
    while not funnet:
        if valgt==varelista[rad][0]:
            vnavn.set(varelista[rad][1])
            vpris.set(varelista[rad][2])
            vkatnr.set(varelista[rad][3])                    
            vantall.set(varelista[rad][4])
            
            if varelista[rad][5]==None:
                vhylle.set('')
            else:
                vhylle.set(varelista[rad][5])
            funnet=True
            
        rad+=1
      
    
    
def lagre_lager():
    
    oppdaterelager_markor=mindatabase.cursor()
    oppdater_tabell=('''UPDATE Vare
                     SET Antall=%s                     
                     WHERE VNr=%s''')
    
    antall=vantall.get()
    varenummer=vnr.get()
    print(varenummer,vnavn,vpris,antall,vkatnr,vhylle)
    oppdater_antall=(antall,varenummer)
    
    

    oppdaterelager_markor.execute(oppdater_tabell,oppdater_antall)   
        

    
    mindatabase.commit()

    
    oppdaterelager_markor.close()

    
    lbl_lagret=Label(window,text='Lagerstatus er oppdatert')
    lbl_lagret.grid(row=4, column=2, padx=5, pady=5, sticky=SE)
    lesing_til_liste()

  


#oprette markører for søking
def lesing_til_liste():
    full_vare_markor=mindatabase.cursor()
    full_vare_markor.execute('SELECT * FROM Vare')

    varelista=[]

    for row in full_vare_markor:
        varelista+=[[row[0],row[1],row[2],row[3],row[4],row[5]]]
        
    full_vare_markor.close()
    return varelista

#kobler mot databasen
mindatabase=mysql.connector.connect(host='localhost',
                                    port=3306,
                                    user='Lagersjefen2022',
                                    passwd='lagerpw',
                                    db='heltnydatabase')
varelista=lesing_til_liste()
#oppretter markør
vare_markor=mindatabase.cursor()

#bruke databasen
vare_markor.execute('SELECT Betegnelse FROM Vare')

#bruke Resultat
#Oppretter en liste basert på Betegnelse/varenavn fra varetabellen

varer=[]
for row in vare_markor:
    varer+=row

window=Tk()
window.title("Endre varebeholdning")

lbl_varenr=Label(window,text='Oppgi varenr: ')
lbl_varenr.grid(row=0, column=0, padx=5, pady=5, sticky=E)
lbl_varenavn=Label(window, text='Varenavn: ')
lbl_varenavn.grid(row=1, column=0, padx=5, pady=5, sticky=E)
lbl_pris=Label(window, text='Pris: ')
lbl_pris.grid(row=2, column=0, padx=5, pady=5, sticky=E)
lbl_katnr=Label(window, text='Kategorinr: ')
lbl_katnr.grid(row=3, column=0, padx=5, pady=5, sticky=E)
lbl_nytt_antall=Label(window, text='Oppgi nytt antall: ')
lbl_nytt_antall.grid(row=4, column=0, padx=5, pady=5, sticky=E)
lbl_hylle=Label(window, text='Hylleplassering: ')
lbl_hylle.grid(row=5, column=0, padx=5, pady=5, sticky=E)

vnr=StringVar()
ent_vnr=Entry(window, width=6, textvariable=vnr)
ent_vnr.grid(row=0, column=1, padx=5, pady=5, sticky=W)
vnavn=StringVar()
ent_vnavn=Entry(window, state='readonly', width=20, textvariable=vnavn)
ent_vnavn.grid(row=1, column=1, padx=5, pady=5, sticky=W)
vpris=StringVar()
ent_vpris=Entry(window, state='readonly', width=5, textvariable=vpris)
ent_vpris.grid(row=2, column=1, padx=5, pady=5, sticky=W)
vkatnr=StringVar()
ent_vkatnr=Entry(window, state='readonly', width=4, textvariable=vkatnr)
ent_vkatnr.grid(row=3, column=1, padx=5, pady=5, sticky=W)
vantall=StringVar()
ent_vantall=Entry(window, width=4, textvariable=vantall)
ent_vantall.grid(row=4, column=1, padx=5, pady=5, sticky=W)
vhylle=StringVar()
ent_vhylle=Entry(window, state='readonly', width=4, textvariable=vhylle)
ent_vhylle.grid(row=5, column=1, padx=5, pady=5, sticky=W)

btn_sjekk=Button(window, text='Sjekk vare', command=hent_vare)
btn_sjekk.grid(row=0, column=3, padx=5, pady=5, sticky=E)

btn_lagre=Button(window, text='Lagre', command=lagre_lager)
btn_lagre.grid(row=4, column=3, padx=5, pady=5, sticky=E)

btn_avslutt=Button(window, text='Avslutt', command=window.destroy)
btn_avslutt.grid(row=5, column=3, padx=5, pady=5, sticky=E)



window.mainloop()

#koble ned databasen

vare_markor.close()
mindatabase.close()