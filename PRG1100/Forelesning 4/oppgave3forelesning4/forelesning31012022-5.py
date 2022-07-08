def heleLista():
    for r in range(0,listelengde,1):
        print()
        print('*********************************Student Personalia*********************************')
        print('Navn: ',student[r][a], student[r][b], '      Studentnr: ',student[r][x],'      Studium: ',student[r][f])
        print()
        print('Fødselsdato: ',student[r][d],'   Epost: ',student[r][c],'    Kjønn: ', student[r][e])
        print()
        print('************************************************************************************')
              

def studentPersonalia():
    print('Fornavn, etternavn og fødselsdato for alle studenter: ')
    print('----------')

    for r in range(listelengde):
        print(student[r][a])
        print(student[r][b])
        print(student[r][d])
        print('----------')
    print()
    
def kvinneStudenter():
    print('Fornavn, etternavn og e-postadresse for alle kvinner: ')
    print('----------')
    for r in range(listelengde):
        if student[r][e]=='Kvinne':
            print(student[r][a])
            print(student[r][b])
            print(student[r][c])
            print('----------')
    print()

def studentIT():
    print('Fornavn, etternavn og kjønn for alle IT&IS studenter:')
    print('----------')
    for r in range(listelengde):
        if student[r][f]=='IT':
            print(student[r][x])
            print(student[r][a])
            print(student[r][b])
            print(student[r][e])
            print('----------')
    print()

def hoved():
    hovedmeny='j'


    while hovedmeny=='j' or hovedmeny=='J':
        print()
        print()
        print('Velg hva du vil skrive ut ifra listen studenter.txt.')
        print('Velg 1 for å skrive ut hele listen.')
        print('Velg 2 for å skrive ut personalia på studenter.')
        print('Velg 3 for å skrive ut kvinnelige studenter.')
        print('Velg 4 for å skrive ut alle IT studenter.')
        print()
        print('Velg 0 for å avslutte program.')
        print('--------------------------------')
        print()
        valg=input('Hva ønsker du og gjøre? ')
        print()
        if valg=='1':
            heleLista()

        if valg=='2':
            studentPersonalia()

        if valg=='3':
            kvinneStudenter()

        if valg=='4':
            studentIT()
            

        if valg=='0':
            print('Du har valgt 0 for avslutting av program')
            print('Program vil nå avsluttes....')
            hovedmeny=0

student=[]
try:
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
    x=0
    a=1
    b=2
    c=3
    d=4
    e=5
    f=6
    hoved()
except:
    print('En feil skjedde ved leting av fil, opprett fil eller endre fil.')

print('Program slutt.')

    
