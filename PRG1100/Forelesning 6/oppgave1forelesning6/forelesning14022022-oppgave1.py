from tkinter import *

def hentPersonalia(event):
    valg=lstStudent.get(lstStudent.curselection())
    
    funnet=False
    radnr=0
    while (funnet==False) and (radnr<=len(student)-1):
        if valg==(student[radnr][0],student[radnr][2]):
            personalia1.set(student[radnr][1])
            personalia2.set(student[radnr][2])
            personalia3.set(student[radnr][3])
            personalia4.set(student[radnr][6])
            funnet=True
        else:
            radnr=radnr+1


student=[]
studentfil=open('studenter.txt','r',encoding='utf-8')

studentnr=studentfil.readline()
while studentnr!='':
    studentnr=studentnr.rstrip('\n')
    fornavn=studentfil.readline().rstrip('\n')
    etternavn=studentfil.readline().rstrip('\n')
    epost=studentfil.readline().rstrip('\n')
    fødselsdato=studentfil.readline().rstrip('\n')
    kjønn=studentfil.readline().rstrip('\n')
    studium=studentfil.readline().rstrip('\n')

    student+=[[studentnr,fornavn,etternavn,epost,fødselsdato,kjønn,studium]]
    
    studentnr=studentfil.readline()

studentfil.close()

listelengde=len(student)

studentlistenr=[]
studentlistenavn=[]
for r in range(0,listelengde,1):
    studentlistenr+=[student[r][0]]
    
for r in range(0,listelengde,1):
    studentlistenavn+=[[student[r][0],student[r][2]]]
    

window=Tk()
window.title('Student')
yScroll=Scrollbar(window,orient=VERTICAL)
yScroll.grid(row=0,column=2,rowspan=5,padx=(0,100),pady=5,sticky=NS)


innholdIlststudent=StringVar()
lstStudent=Listbox(window,width=30,height=5,listvariable=innholdIlststudent,yscrollcommand=yScroll.set)
lstStudent.grid(row=0,column=1,rowspan=5,padx=(100,0),pady=5,sticky=E)
innholdIlststudent.set(tuple(studentlistenavn))
yScroll["command"]=lstStudent.yview

personalia1=StringVar()
entPersonalia1=Entry(window,width=30,state="readonly",textvariable=personalia1)
entPersonalia1.grid(row=0,column=3,sticky=E)
personalia2=StringVar()
entPersonalia2=Entry(window,width=30,state="readonly",textvariable=personalia2)
entPersonalia2.grid(row=1,column=3,sticky=E)
personalia3=StringVar()
entPersonalia3=Entry(window,width=30,state="readonly",textvariable=personalia3)
entPersonalia3.grid(row=2,column=3,sticky=E)
personalia4=StringVar()
entPersonalia4=Entry(window,width=30,state="readonly",textvariable=personalia4)
entPersonalia4.grid(row=3,column=3, sticky=E)
lstStudent.bind("<<ListboxSelect>>", hentPersonalia)

btnAvslutt=Button(window,text='Avslutt',command=window.destroy)
btnAvslutt.grid(row=5,column=1,padx=5,pady=25,sticky=E)

window.mainloop()