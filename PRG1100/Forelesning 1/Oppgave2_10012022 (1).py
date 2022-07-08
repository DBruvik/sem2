def main():    
    
    
    status,studentnr=sjekk_student()
    
    
    if status==True and studentnr!='':
        skriv_karakterliste(studentnr)
    else:
        print('Studenten finnes ikke')


def skriv_karakterliste(skriv_karakterlisteStudentnr):
   
        studentfil=open('student.txt','r')        

        #lager bools variabel for å kontrolere løkka
        student_i_databasen=False
        
        #les første linje i student.txt
        student=studentfil.readline()

        #printer studentopplysninger som har blitt lest av fra POST
        while student!='' and student_i_databasen==False:
            student=student.rstrip('\n')
            if student==skriv_karakterlisteStudentnr:
                fornavn=studentfil.readline().rstrip('\n')
                etternavn=studentfil.readline().rstrip('\n')
                studium=studentfil.readline().rstrip('\n')
                print('----------------------------------------------------------------------')
                print()
                print('Studentopplysninger:')
                print()
                print('Studentnr:')
                print(student)
                print()
                print('Navn og etternavn:')
                print(fornavn,etternavn)
                print()
                print('Studium:')
                print(studium)
                student_i_databasen=True                
            else:
                #leser resten av Posten
                student=studentfil.readline()
                student=studentfil.readline()
                student=studentfil.readline()

                #leser første linja i neste POST
                student=studentfil.readline()
                
        #stenger fila
        studentfil.close()        
        
        if not student_i_databasen:
            print('----------------------------------------------------------------------')
            print()
            print('Studenten er ikke registrert i databasen.')
            print()            
        else:
            #lager variabel for å kontrollere om studenten har karakter
            student_med_karakter=False
            
            #åpner eksamensresultater i read
            resultatfil=open('eksamensresultat.txt','r')                      
            print('----------------------------------------------------------------------')
            print()
            print('Eksamensresultater:')
            print()
            
            #kobler emnekode med emnenavn, og skriver ut karakter
            #løkka kjører til EOF
            emnekode=resultatfil.readline()
            while emnekode!='':
                #leser hele POST
                emnekode=emnekode.rstrip('\n')
                student=resultatfil.readline().rstrip('\n')
                karakter=resultatfil.readline().rstrip('\n')
                #hvis studentnr er det samme som studentnr i POST
                #henter emnenavn via emnekode
                if student==skriv_karakterlisteStudentnr:
                    emnefil=open('emne.txt','r')
                    emnekode_i_emnefil=emnefil.readline()                    
                    while emnekode_i_emnefil!='':
                        #rstriper slik at emnekode_i_emnefil kan sammenlignes med emnekode
                        emnekode_i_emnefil=emnekode_i_emnefil.rstrip('\n')
                        if emnekode==emnekode_i_emnefil:
                            emnenavn=emnefil.readline().rstrip('\n')
                            print(emnekode,emnenavn,karakter)
                            emnekode_i_emnefil=emnefil.readline()
                        else:
                            emnekode_i_emnefil=emnefil.readline()
                    emnefil.close()
                    emnekode=resultatfil.readline()
                    student_med_karakter=True                                    
                else:
                    emnekode=resultatfil.readline()
                    
            #stenger resultatfila    
            resultatfil.close()
        
        if not student_med_karakter and student_i_databasen==True:
            print()
            print('Studenten har ingen registrerte eksamensresultater.')
            print()

def sjekk_student():
    studnr=input('Hva er studentnr? ')
    studentfil=open('student.txt','r')
    funnet=False
    student=studentfil.readline()
    while student!='' and funnet==False:
            student=student.rstrip('\n')
            if studnr==student:                
                funnet=True
            else:
                student=studentfil.readline()
    studentfil.close()

    
    return funnet,studnr
            

main()
   
