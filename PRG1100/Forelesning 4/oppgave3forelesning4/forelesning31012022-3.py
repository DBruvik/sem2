student=[]
print(student)
print()

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

print('Resultatet ble:', student)
print()
x=0
a=1
b=2
c=3
d=4
e=5
f=6

listelengde=len(student)

print('test')
for r in range(listelengde):
    print(student[r])

print('Fornavn, etternavn og fødselsdato for alle studenter: ')
print('----------')

for r in range(listelengde):
    print(student[r][a])
    print(student[r][b])
    print(student[r][d])
    print('----------')
print()

print('Fornavn, etternavn og e-postadresse for alle kvinner: ')
print('----------')
for r in range(listelengde):
    if student[r][e]=='Kvinne':
        print(student[r][a])
        print(student[r][b])
        print(student[r][c])
        print('----------')

print('Fornavn, etternavn og kjønn for alle IT&IS studenter:')
print('----------')
for r in range(listelengde):
    if student[r][f]=='IT':
        print(student[r][x])
        print(student[r][a])
        print(student[r][b])
        print(student[r][e])
        print('----------')
       
