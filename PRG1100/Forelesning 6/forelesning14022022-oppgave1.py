from tkinter import *

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

studentliste=[]
for r in range(0,listelengde,1):
    studentliste+=[student[r][0],student[r][2]]

window=Tk()
window.title('Student')
innholdIlststudent=StringVar()
lstStudent=Listbox(window,widht=10,height=5,listevariable=innholdIlststudent)
lstStudent.grid(padx=100,pady=5)
innholdIlststudent.set(tuple(studentnr,etternavn))

window.mainloop()
