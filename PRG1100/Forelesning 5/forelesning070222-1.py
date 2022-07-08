#PGR1100-2022-strengmanipulasjon

ansatte=[]
print(ansatte)
print()

ansattfil=open('Laerer.txt','r', encoding='utf-8')

fornavn=ansattfil.readline()
while fornavn!='':
    fornavn=fornavn.rstrip('\n')
    etternavn=ansattfil.readline().rstrip('\n')
    epost=ansattfil.readline().rstrip('\n')

    ansatte+=[[fornavn,etternavn,epost]]

    fornavn=ansattfil.readline()

ansattfil.close()

print(ansatte)
print()

listelengde=len(ansatte)
print(listelengde)
print()

print('Initialer og e-post adresser')
for in range(listelengde):
    print(ansatte[r][0][0:1],ansatte[r][1][0:1],'har e-postadresse',ansatte[r][2])
    
