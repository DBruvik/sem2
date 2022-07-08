from tkinter import *

ansatte=[]
ansattfil=open('Laerer.txt','r',encoding='utf-8')
fornavn=ansattfil.readline()

while fornavn!='':
    fornavn=fornavn.rstrip('\n')

    etternavn=ansattfil.readline().rstrip('\n')
    epost=ansattfil.readline().rstrip('\n')

    ansatte+=[[fornavn,etternavn,epost]]

    fornavn=andsattfil.readline()

ansattfil.close()

fornavn=[]
for listelengde in range(0,len(ansatte),1):
    fornavn+=[ansatte[listelengde][0]]

    window=Tk()
    window.title('Ansatte')

    innhold_i_lst_ansatte=StringVar()
    lst_ansatte=Listbox(window,width=10,height=5,listvariable=innhold_i_lst_ansatte)
    lst_ansatte.grid(padx=199,pady=5)
    innhold_i_lst_ansatte.set(tuple(fornavn))

    window.mainloop()
    
