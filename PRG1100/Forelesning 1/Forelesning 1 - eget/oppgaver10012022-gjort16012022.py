import os


def leggTil():
    nyStudent='j'
    print('Du har valgt 1, registrering av studentnummer.')
    print()
    while nyStudent=='j' or nyStudent=='J':
        studentEksisterer=False
        while studentEksisterer==False:

            studentnr=input('Skriv inn studentnummer eller n/N for å gå tilbake til hovedmeny:')

            studentfil=open('student.txt','r')
            soket=studentfil.readline()
            #
            if studentnr=='n' or studentnr=='N':
                nyStudent=0
                studentEksisterer=True
                soket=''
                print()
                print('Tilbake til hovedmeny')
                print()
            #
            while soket!='':
                soket=soket.rstrip('\n')

                if soket==studentnr:
                    print('Student nummer',studentnr,'finnes allerede i registeret og lagres ikke.')
                    studentEksisterer=True
                soket=studentfil.readline()

            studentfil.close()
            #
            if not studentEksisterer:
                studentfil=open('student.txt','a')
                print('Registrerer', studentnr)
                fornavn=input('Skriv inn fornavn på student: ')
                etternavn=input('Skriv inn etternavn på student: ')
                studium=input('Skriv inn studim på student: ')

                    #
                studentfil.write(studentnr+'\n')
                studentfil.write(fornavn+'\n')
                studentfil.write(etternavn+'\n')
                studentfil.write(studium+'\n')
                print('Studenten er nå lagret!')
                studentEksisterer=True
                #Studentopplysningene er lagt til i student.txt og spør om du vil legge til fler
                studentfil.close()
                print('j/J for å legge til ny student eller n/N for å gå til hovedmeny')
                nyStudent=input('Vil du legge til flere studenter? ')



def slett():
    print('Du har valgt 2, sletting av student.')
    print()
    brukerOnskerSletting='j'
    while brukerOnskerSletting=='j' or brukerOnskerSletting=='J':
        studentEksisterer=False
        while studentEksisterer==False:

            studentnr=input('Skriv inn studentnummer for sletting eller n/N for å avslutte:')
            studentfil=open('student.txt','r')
            studentRegisterStudentnr=studentfil.readline()
            if studentnr=='n' or studentnr=='N':
                brukerOnskerSletting=''
                studentEksisterer=''
                studentRegisterStudentnr=''
                print()
                print('Tilbake til hovedmeny')

            while studentRegisterStudentnr!='':
                studentRegisterStudentnr=studentRegisterStudentnr.rstrip('\n')
                studentRegisterFornavn=studentfil.readline().rstrip('\n')
                studentRegisterEtternavn=studentfil.readline().rstrip('\n')
                studentRegisterStudium=studentfil.readline().rstrip('\n')

                if studentRegisterStudentnr==studentnr:
                    studentEksisterer=True
                studentRegisterStudentnr=studentfil.readline()
            studentfil.close()

            if studentEksisterer:
                studentHarEksamenResultat=False

                eksamenfil=open('eksamensresultat.txt','r')
                emnekode=eksamenfil.readline()

                while emnekode!='':
                    emnekode=emnekode.rstrip('\n')
                    eksamenStudentnr=eksamenfil.readline().rstrip('\n')
                    eksamenKarakter=eksamenfil.readline().rstrip('\n')

                    if eksamenStudentnr==studentnr:
                        studentHarEksamenResultat=True

                    emnekode=eksamenfil.readline()
                eksamenfil.close()

                if studentHarEksamenResultat:
                    print('Studenten', studentnr,'har 1 eller flere eksamenskarakterer og kan derfor ikke slettes')

                else:
                    print('Det er ikke registrert noen karakterer på studenten.')
                    angre=input('Er du sikker på at du vil slette student tast j/J, eller alt annet for å avbryte: ')
                    if angre=='j' or angre=='J':
                        tempfil=open('temp.txt','w')
                        studentfil=open('student.txt','r')
                        studentRegisterStudentnr=studentfil.readline()

                        while studentRegisterStudentnr!='':
                            studentRegisterStudentnr=studentRegisterStudentnr.rstrip('\n')
                            studentRegisterFornavn=studentfil.readline().rstrip('\n')
                            studentRegisterEtternavn=studentfil.readline().rstrip('\n')
                            studentRegisterStudium=studentfil.readline().rstrip('\n')

                            if studentRegisterStudentnr!=studentnr:
                                tempfil.write(studentRegisterStudentnr+'\n')
                                tempfil.write(studentRegisterFornavn+'\n')
                                tempfil.write(studentRegisterEtternavn+'\n')
                                tempfil.write(studentRegisterStudium+'\n')
                                    
                            StudentRegisterStudentnr=studentfil.readline()
                        studentfil.close()
                        tempfil.close()

                        os.remove('student.txt')
                        os.rename('temp.txt','student.txt')

                        print()
                        print('Studenten er slettet og student.txt er oppdatert')

                    else:
                        print('Du har avsluttet sletting.')
                        brukerOnskerSletting='j'

            else:
                if not studentEksisterer:
                    print('Studenten finnes ikke i registeret')
                if studentnr=='n' or studentnr=='N':
                    print()
                                

def karakterUtskrift():
    print('Du har valgt 3, utskrift av karakterer.')
    print()
    brukerOnskerUtskrift='j'
    while brukerOnskerUtskrift=='j' or brukerOnskerUtskrift=='J':
        studentEksisterer=False
        while not studentEksisterer:
            studentnr=input('Skriv inn studentnummer for utskrift eller n/N for å gå tilbake til hovedmeny: ')

            studentfil=open('student.txt','r')
            studentRegisterStudentnr=studentfil.readline()
            studentNavn=''
            studentStudium=''
            if studentnr=='n' or studentnr=='N':
                brukerOnskerUtskrift=0
                studentEksisterer=True
                studentRegisterStudentnr=''
                print()
                print('Tilbake til hovedmeny')
                #søker etter student
            while studentRegisterStudentnr!='':
                studentRegisterStudentnr=studentRegisterStudentnr.rstrip('\n')
                studentRegisterFornavn=studentfil.readline().rstrip('\n')
                studentRegisterEtternavn=studentfil.readline().rstrip('\n')
                studentRegisterStudium=studentfil.readline().rstrip('\n')

                if studentRegisterStudentnr==studentnr:
                    studentNavn=(studentRegisterFornavn+ ' ' +studentRegisterEtternavn)
                    studentStudium=studentRegisterStudium
                    studentEksisterer=True
                studentRegisterStudentnr=studentfil.readline()
            studentfil.close()

            if studentEksisterer:
                studentHarEksamenResultat=False

                eksamenfil=open('eksamensresultat.txt','r')
                emnekode=eksamenfil.readline()

                while emnekode!='':
                    emnekode=emnekode.rstrip('\n')
                    eksamenStudentnr=eksamenfil.readline().rstrip('\n')
                    eksamenKarakter=eksamenfil.readline().rstrip('\n')

                    if eksamenStudentnr==studentnr:
                        studentHarEksamenResultat=True

                    emnekode=eksamenfil.readline()
                eksamenfil.close()
                
                if studentHarEksamenResultat:
                    print('--------------------------------')
                    print(studentNavn,studentStudium,studentnr)
                    eksamenfil=open('eksamensresultat.txt','r')
                    emnekode=eksamenfil.readline()

                    while emnekode!='':
                        emnekode=emnekode.rstrip('\n')
                        eksamenStudentnr=eksamenfil.readline().rstrip('\n')
                        eksamenKarakter=eksamenfil.readline().rstrip('\n')

                        if eksamenStudentnr==studentnr:
                            emnefil=open('emne.txt','r')
                            emneRegisterEmnekode=emnefil.readline()
                            emnenavn=''
                            while emneRegisterEmnekode!='':
                                emneRegisterEmnekode=emneRegisterEmnekode.rstrip('\n')
                                emneRegisterEmnenavn=emnefil.readline().rstrip('\n')

                                if emneRegisterEmnekode==emnekode:
                                    emnenavn=emneRegisterEmnenavn

                                emneRegisterEmnekode=emnefil.readline()
                            emnefil.close()

                            print(emnekode,emnenavn,eksamenKarakter)

                        emnekode=eksamenfil.readline()
                    eksamenfil.close()

                else:
                    if studentnr=='n' or studentnr=='N':
                        print()
                    else:
                        print('Studentnummeret finnes IKKE i eksamenresultat.txt og har ingen eksamensresultater.')
                        print()
            else:
                print('Studentnummeret finnes ikke i stundet.txt.')
                



#Hovedprogrammet/Hovedmenyen i eget delprogram
def hoved():
    hovedmeny='j'


    while hovedmeny=='j' or hovedmeny=='J':
        print('--------------------------------')
        print('Velkommen til Studieadministrativt systemets hovedside.')
        print('Velg 1 for å legge til ny student.')
        print('Velg 2 for å slette student.')
        print('Velg 3 for å skrive ut karakterer til student.')
        print()
        print('Velg 0 for å avslutte program.')
        print('--------------------------------')
        print()
        valg=input('Hva ønsker du og gjøre? ')
        print()
        if valg=='1':
            leggTil()

        if valg=='2':
            slett()

        if valg=='3':
            studentnr=input('Skriv inn student nummer på student du ønsker utskrift for: ')
            studentfil=open('student.txt','r')
            nr=studentfil.readline()

            while nr!='':
                nr=nr.rstrip('\n')
                fornavn=studentfil.readline().rstrip('\n')
                etternavn=studentfil.readline().rstrip('\n')
                studium=studentfil.readline().rstrip('\n')
                if nr==studentnr:
                    print('Denne studenten er gyldig.')
                    print()
                    eksisterer=True
                    skrivKarakterliste(studentnr)
                nr=studentfil.readline()
            karakterUtskrift()

        if valg=='0':
            print('Du har valgt 0 for avslutting av program')
            print('Program vil nå avsluttes....')
            hovedmeny=0
hoved()
print('Programmet er avsluttet.')
