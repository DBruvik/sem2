#Oppgave 1 fra forelsening


navn=[]
print(navn)
print()

fornavnfil=open('fornavn.txt','r',encoding='utf-8')

fornavn=fornavnfil.readline()
while fornavn!='':
    fornavn=fornavn.rstrip('\n')

    navn+=[fornavn]

    fornavn=fornavnfil.readline()

fornavnfil.close()

print('Resultatet ble:', navn)

listelengde=len(navn)
print(listelengde)

for r in range(listelengde):
    print('Gjennomgang nr:',r+1)
    for sjekk in range(0,listelengde-1,1):
        if navn[sjekk]>navn[sjekk+1]:
            bytte=navn[sjekk]
            navn[sjekk]=navn[sjekk+1]
            navn[sjekk+1]=bytte
            print('Sjekk nr:',sjekk+1)
            print('Lista så langt:',navn)
            
print('Den sorterte lista er:', navn)

sortertNavn=open('sortertnavn.txt','w')

for navn in navn:
    sortertNavn.write(navn+'\n')

sortertNavn.close()

