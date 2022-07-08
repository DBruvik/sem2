import os
from tkinter import *

mindatabase=0
Toplevel=0
messagebox=0
Label=0


def endre_eks_resultat():
    def hent_resultater():
        studentnr=vstudentnr.get()
        dato=vdato.get()

        hent_resultater_markor=mindatabase.cursor()

        hent_resultater_lst_boks_data=('''SELECT Emnekode
                                          FROM Eksamensresultat
                                          WHERE Studentnr=%s AND Dato=%s''')
                                         
        hent_resultater_markor.execute(hent_resultater_lst_boks_data,(studentnr,dato,))

        emnekode_liste=[]
        for r in hent_resultater_markor:
            emnekode_liste+=[r[0]]
        
        innholds_lst_emnekoder.set(emnekode_liste)

        print(innholds_lst_emnekoder)  
        hent_resultater_markor.close()

    def endre_eks_resultat_boks(event):
        endre_eks_resultat_valgt=lst_emnekode.get(lst_emnekode.curselection())

        r=0
        funnet=False
        while funnet==False:
            if endre_eks_resultat_valgt==eksamensresultat_liste[r][1] and vstudentnr.get()==eksamensresultat_liste[r][0]:
                vemnekode.set(endre_eks_resultat_valgt)
                vkarakter.set(eksamensresultat_liste[r][2])
                funnet=True
            r+=1  


    
    def endring_eks_resultat():
        endre_markor=mindatabase.cursor()
        
        bytte_opplysning=('''UPDATE Eksamensresultat SET Karakter=%s
                             WHERE Studentnr=%s AND Dato=%s AND Emnekode=%s''')

        karakter=vkarakter.get()
        studentnr=vstudentnr.get()
        dato=vdato.get()
        emnekode=vemnekode.get()

        oppdat_eks_resultat=(karakter,studentnr,dato,emnekode)

        endre_markor.execute(bytte_opplysning,oppdat_eks_resultat)

        mindatabase.commit()
        endre_markor.close()
        
        messagebox.showinfo(message='Karakter oppdatering gjennomført!')
        hent_resultater()

    
    endre_eks_resultat_vindu=Toplevel()
    endre_eks_resultat_vindu.title('Endre eksamensresultat')
    
    y_scroll=Scrollbar(endre_eks_resultat_vindu,orient=VERTICAL)
    y_scroll.grid(row=0,column=1,rowspan=10,padx=(0,20),pady=5,sticky=NS)

    innholds_lst_emnekoder=StringVar()
    lst_emnekode=Listbox(endre_eks_resultat_vindu,width=40,height=10,listvariable=innholds_lst_emnekoder,
                        yscrollcommand=y_scroll.set)
    lst_emnekode.grid(row=0,column=0,rowspan=10,padx=(0,50),pady=5,sticky=E)
    y_scroll['command']=lst_emnekode.yview
    
    label_eks_resultat_studentnr=Label(endre_eks_resultat_vindu,text='Tast inn studentnr:' )
    label_eks_resultat_studentnr.grid(row=0,column=2,padx=5,pady=5,sticky=E)


    label_eks_dato=Label(endre_eks_resultat_vindu,text='Skriv inn dato(AAMMDD):' )
    label_eks_dato.grid(row=1,column=2,padx=5,pady=5,sticky=E)

    label_eks_resultat_karakter=Label(endre_eks_resultat_vindu, text='Tast inn Karakter arakter(A-F):' )
    label_eks_resultat_karakter.grid(row=3,column=2,padx=5,pady=5,sticky=E)

    label_eks_resultat_emnekode=Label(endre_eks_resultat_vindu,text='Valgt emnekode:')
    label_eks_resultat_emnekode.grid(row=4,column=2,padx=5,pady=5,sticky=E)



    vstudentnr=StringVar()
    ent_studentnr=Entry(endre_eks_resultat_vindu,width=6,textvariable=vstudentnr)
    ent_studentnr.grid(row=0,column=3,padx=5,pady=5,sticky=W)


    vdato=StringVar()
    ent_vdato=Entry(endre_eks_resultat_vindu,width=10,textvariable=vdato)
    ent_vdato.grid(row=1,column=3,padx=5,pady=5,sticky=W)

    vkarakter=StringVar()
    ent_vkarakter=Entry(endre_eks_resultat_vindu,width=2,textvariable=vkarakter)
    ent_vkarakter.grid(row=3,column=3,padx=5,pady=5,sticky=W)

    vemnekode=StringVar()
    ent_vemnekode=Entry(endre_eks_resultat_vindu,width=8,state='readonly',textvariable=vemnekode)
    ent_vemnekode.grid(row=4,column=3,padx=5,pady=15,sticky=W)

    btn_hent_eks_resultat_emnekode=Button(endre_eks_resultat_vindu,text='Hent emnekoder',command=hent_resultater)
    btn_hent_eks_resultat_emnekode.grid(row=0,column=4,padx=5,pady=5,sticky=W)

    btn_lagre=Button(endre_eks_resultat_vindu,width=20,text='Lagre eksamensresultat',command=endring_eks_resultat)
    btn_lagre.grid(row=7,column=3,padx=5,pady=5,sticky=S)
    
    btn_tilbake=Button(endre_eks_resultat_vindu,width=20,text='Tilbake til menyen',command=endre_eks_resultat_vindu.destroy)
    btn_tilbake.grid(row=7,column=4,padx=5,pady=5,sticky=S)

    studentnummer=vstudentnr.get()

    endre_eks_resultat_markor=mindatabase.cursor()
    endre_eks_resultat_data=('''SELECT Studentnr,Emnekode,Karakter
                                         FROM Eksamensresultat''')

    eksamensresultat_liste=[]

    for row in endre_eks_resultat_markor:
        eksamensresultat_liste+=[[row[0],row[1],row[2]]]
    

    print(eksamensresultat_liste)

    lst_emnekode.bind('<<ListboxSelect>>',endre_eks_resultat_boks)