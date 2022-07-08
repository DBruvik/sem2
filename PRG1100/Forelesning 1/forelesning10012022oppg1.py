import os

#Delprogram for registrering/legge til nye studenter i fil
def leggTil():
    nyStudent='j'
    print('Du har valgt 1, registrering av studentnummer.')
    print()
    while nyStudent=='j' or nyStudent=='J':
        studentEksisterer=False
        while studentEksisterer==False:
        
            studentnr=input('Skriv inn studentnummer eller n/N for å gå tilbake til hovedmeny: ')
           
            studentfil=open('student.txt','r')
            soket=studentfil.readline()
            #Testing på avslutte delprogram
            if studentnr=='n' or studentnr=='N':
                nyStudent=0
                studentEksisterer=True
                soket=''
                print()
                print('Tilbake til hovedmeny')
                print()
            #Søker etter student
            while soket!='':
                soket=soket.rstrip('\n')

                if soket==studentnr:
                    print('Student nummer',studentnr,'finnes allerede i registret og lagres ikke.')
                    studentEksisterer=True
                soket=studentfil.readline()
        
            studentfil.close()
            #Studentnr eksisterer ikke i student.txt
            if not studentEksisterer:
                studentfil=open('student.txt','a')
                print('Registrerer', studentnr)
                fornavn=input('Skriv inn fornavn på student: ')
                etternavn=input('Skriv inn etternavn på student: ')
                studium=input('Skriv inn studim på student: ')

                #Skriver inn studentopplysningene
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


#Delprogram for sletting av studenter i fil          
def slett():
    print('Du har valgt 2, sletting av student.')
    print()
    brukerOnskerSletting='j'
    while brukerOnskerSletting=='j' or brukerOnskerSletting=='J':
        studentEksisterer=False
        while studentEksisterer==False:
            
            studentnr=input('Skriv inn studentnummer for sletting eller n/N for å gå tilbake til hovedmeny: ')
            #Åpner fil, dersom studentnr=n/N vil variablene bli satt for å stoppe prosessen "slett()" og fil lukkes  
            studentfil=open('student.txt','r')
            studentRegisterStudentnr=studentfil.readline().rstrip('\n')
            #Testing på å avslutte delprogram
            if studentnr=='n' or studentnr=='N':
                brukerOnskerSletting=''
                studentEksisterer=''
                studentRegisterStudentnr=''
                print()
                print('Tilbake til hovedmeny.')
            #Søker etter studentnr i student.txt
            while studentRegisterStudentnr!='':
                studentRegisterFornavn=studentfil.readline().rstrip('\n')
                studentRegisterEtternavn=studentfil.readline().rstrip('\n')
                studentRegisterStudium=studentfil.readline().rstrip('\n')
                                                                
                #Dersom studentnr eksisterer blir variabel satt til sann/True
                if studentRegisterStudentnr==studentnr:
                    studentEksisterer=True
                studentRegisterStudentnr=studentfil.readline().rstrip('\n')
            studentfil.close()
              #Studenten er funnet i student.txt, setter eksamensresultat variabel, for og teste senere
            if studentEksisterer:
                studentHarEksamenResultat=False
                #Sjekker om det er registrert eksamensresultat på studentnr i eksamenresultat.txt
                eksamenfil=open('eksamensresultat.txt','r')
                emnekode=eksamenfil.readline().rstrip('\n')
                
                
                while emnekode!='':
                    eksamenStudentnr=eksamenfil.readline().rstrip('\n')
                    eksamenKarakter=eksamenfil.readline().rstrip('\n')

                    if eksamenStudentnr==studentnr:
                        studentHarEksamenResultat=True
                        
                    emnekode=eksamenfil.readline().rstrip('\n')
                    #Lukker filen
                eksamenfil.close()
                #Sjekker om studentnr har resultat i eksamenresultat.txt     
                if studentHarEksamenResultat==True:
                    print('Studenten',studentnr, 'har 1 eller flere eksamenskarakterer registrert og kan derfor ikke slettes.')
                    
                #Ingen resultater registrert, starter selve prosessen om å slette/skrive om student.txt til temp.txt
                else:
                    print('Det er ikke registrert noen karakterer på studenten.')
                    #Kontroll bare, ekstra sikkerhet dersom feil er gjort.
                    angre=input('Er du sikker på at du vil slette student tast j/J eller alt annet for å avbryte: ')
                    if angre=='j' or angre=='J':
                        tempfil=open('temp.txt','w')
                        studentfil=open('student.txt','r')
                        studentRegisterStudentnr=studentfil.readline().rstrip('\n')
                        #søker etter studentnr i student.txt for å finne det som skal fjernes
                        
                        while studentRegisterStudentnr!='':
                            studentRegisterFornavn=studentfil.readline().rstrip('\n')
                            studentRegisterEtternavn=studentfil.readline().rstrip('\n')
                            studentRegisterStudium=studentfil.readline().rstrip('\n')
                                                                            
                            #Dersom studentnr ikke er lik søket skal det skrives om i temp.txt med samme data utenom det som er likt som studentnr
                            if studentRegisterStudentnr!=studentnr:
                                tempfil.write(studentRegisterStudentnr+'\n')
                                tempfil.write(studentRegisterFornavn+'\n')
                                tempfil.write(studentRegisterEtternavn+'\n')
                                tempfil.write(studentRegisterStudium+'\n')
                            studentRegisterStudentnr=studentfil.readline().rstrip('\n')
                            
                        studentfil.close()
                        tempfil.close()
                        #Lukker og fjerner student.txt og døper om temp.txt til student.txt som ny fil med slettet student.
                        os.remove('student.txt')
                        os.rename('temp.txt', 'student.txt')
                        print()
                        print('Studenten er slettet og student.txt er oppdatert.')
                    else:
                        print('Du har nå avbrutt sletting.')
                        brukerOnskerSletting='j'
                        
            else:
                if studentEksisterer==False:
                    print('Studenten finnes IKKE i registeret.')
                if studentnr=='n' or studentnr=='N':
                    print()


#Delprogram for utskrift av karakterer på studenter fra fil
def skrivKarakterliste(skriv_karakterlisteStudentnr):
    finn=True
    
    while finn==True:
        funnet=False
        
        studentfil=open('student.txt','r')
        student=studentfil.readline()
        while student!='':
            student=student.rstrip('\n')
            fornavn=studentfil.readline().rstrip('\n')
            etternavn=studentfil.readline().rstrip('\n')
            studium=studentfil.readline().rstrip('\n')
            if student==skriv_karakterlisteStudentnr:
                print(student+'',fornavn+'',etternavn+'',studium)
            student=studentfil.readline()
            
        studentfil.close()
        karakter=open('eksamensresultat.txt','r')
        emne=open('emne.txt','r')
        tempkarakter=open('temp.txt','w')
        emnekodekarakter=karakter.readline()
        emnekodeemne=emne.readline()
        emnefillesing=False
        emneliste=[]
        while emnefillesing==False:
                emnekodeemne=emnekodeemne.rstrip('\n')
                emnenavn=emne.readline().rstrip('\n')
                emneliste+=[emnekodeemne]
                emneliste+=[emnenavn]
                emnekodeemne=emne.readline()
                if emnekodeemne=='':
                    emnefillesing=True
                
        while emnekodekarakter !='':
            emnekodekarakter=emnekodekarakter.rstrip('\n')
            student=karakter.readline().rstrip('\n')
            eksamenskarakter=karakter.readline().rstrip('\n')
            
            if skriv_karakterlisteStudentnr==student:
                tempkarakter.write(emnekodekarakter+'\n')
                emnefunnet=False
                emneindeks=0
                
                while emnefunnet==False:
                    if emnekodekarakter==emneliste[emneindeks]:
                        tempkarakter.write(emneliste[emneindeks+1]+'\n')
                        emnefunnet=True
                    emneindeks=emneindeks+2
                    
                tempkarakter.write(eksamenskarakter+'\n')
            
            emnekodekarakter=karakter.readline()
    
        tempkarakter.close()
        tempkarakter=open('temp.txt','r')
        emnekodekarakter=tempkarakter.readline()
        while emnekodekarakter!='':
            emnekodekarakter=emnekodekarakter.rstrip('\n')
            navn=tempkarakter.readline().rstrip('\n')
            resultat=tempkarakter.readline().rstrip('\n')
            print(emnekodekarakter,navn,resultat)
            emnekodekarakter=tempkarakter.readline()
        tempkarakter.close()
        karakter.close()
        emne.close()
        os.remove('temp.txt')
        print()
        finn=False
            
        


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
        valg=input('Velg noe:')
        print()
        if valg=='1':
            leggTil()

        if valg=='2':
            slett()

        if valg=='3':
            studentnr=input('Skriv inn studentnr på student du vil ha utskrift for: ')
            studentfil=open('student.txt','r')
            nr=studentfil.readline()

            while nr!='':
                nr=nr.rstrip('\n')
                fornavn=studentfil.readline().rstrip('\n')
                etternavn=studentfil.readline().rstrip('\n')
                studium=studentfil.readline().rstrip('\n')
                if nr==studentnr:
                    print('Denne studenten er gyldig')
                    print()
                    eksisterer=True
                    skrivKarakterliste(studentnr)
            
                nr=studentfil.readline()  
            studentfil.close()
            

        if valg=='0':
            print('Du har valgt 0 for avslutting av program')
            print('Program vil nå avsluttes....')
            hovedmeny=0
hoved()
print('Programmet er avsluttet.')
    
