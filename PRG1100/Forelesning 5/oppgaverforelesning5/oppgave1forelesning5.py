def heleLista():
    for r in range(0,listelengde,1):
        print()
        print('*********************************Student Personalia*********************************')
        print('Navn: ',student[r][1], student[r][2], '      Studentnr: ',student[r][0],'      Studium: ',student[r][6])
        print()
        print('Fødselsdato: ',student[r][4],'   Epost: ',student[r][3],'    Kjønn: ', student[r][5])
        print()
        print('************************************************************************************')
              

def studentPersonalia():
    print('Fornavn, etternavn og fødselsdato for alle studenter: ')
    print('----------')

    for r in range(listelengde):
        print(student[r][1])
        print(student[r][2])
        print(student[r][4])
        print('----------')
    print()
    
def kvinneStudenter():
    print('Fornavn, etternavn og e-postadresse for alle kvinner: ')
    print('----------')
    for r in range(listelengde):
        if student[r][e]=='Kvinne':
            print(student[r][1])
            print(student[r][2])
            print(student[r][3])
            print('----------')
    print()

def studentIT():
    print('Fornavn, etternavn og kjønn for alle IT&IS studenter:')
    print('----------')
    for r in range(listelengde):
        if student[r][f]=='IT':
            print(student[r][0])
            print(student[r][1])
            print(student[r][2])
            print(student[r][5])
            print('----------')
    print()


def antallKvinner():
    print('Teller antall kvinner')
    antall=0
    for key in student:
        print(key,student[key][0])
        kjonn=student[key][4]
        if kjonn=='Kvinne':
            antall+=1

    print('Antall kvinner funnet er: ', antall)

def antallStudenterStudium():
    antallIt=0
    antallOkad=0
    for key in student:
        print(key,student[key][0])
        studenter=student[key][5]
        if studenter=='IT':
            antallIt+=1
        if studenter=='Økad':
            antallOkad+=1

    print('Antall IT studenter: ',antallIt)
    print('Antall Økad studenter: ', antallOkad)
    


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
        print('Velg 5 for å telle antall kvinner i fil.')
        print('Velg 6 for å telle IT og Økad studenter.')
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

        if valg=='5':
            antallKvinner()

        if valg=='6':
            antallStudenterStudium()

        if valg=='0':
            print('Du har valgt 0 for avslutting av program')
            print('Program vil nå avsluttes....')
            hovedmeny=0

student={}
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

        student[studentnr]=[fornavn,etternavn,epost,fødselsdato,kjønn,studium]
        
        studentnr=studentfil.readline()

    studentfil.close()

    listelengde=len(student)
    hoved()
except:
    print('En feil skjedde ved leting av fil, opprett fil eller endre fil.')

print('Program slutt.')

    
