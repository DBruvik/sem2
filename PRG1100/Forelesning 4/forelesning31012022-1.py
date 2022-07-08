#PRG1100 2-dimesjonal tabell

ansatte=[]
print(ansatte)
print()

ansattfil=open('Laerer.txt','r',encoding='utf-8')

fornavn=ansattfil.readline()

while fornavn!='':
    fornavn=fornavn.rstrip('\n')


    etternavn=ansattfil.readline().rstrip('\n')
    epost=ansattfil.readline().rstrip('\n')

    ansatte+=[[fornavn,etternavn,epost]]

    fornavn=ansattfil.readline()

ansattfil.close()





print('Resultatet ble:',ansatte)
print()

print(ansatte[4])
print()

print(ansatte[4][2])
print()

listelengde=len(ansatte)
print(listelengde)
print()

print('Etternavn:')
c=1
for r in range (listelengde):
    print(ansatte[r][c])
print()

print('Etternavn og epostadresser:')
c=1
for r in range(listelengde):
    print(ansatte[r][c],'har e-postadresse',ansatte[r][c+1])
print()

