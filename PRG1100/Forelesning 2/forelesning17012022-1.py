#Oppgave 3 ifra første forelesning
#Sjekk EOF/int value
try:
    tekstfil=open('tall.txt','r')
    total=0
    count=0
    for line in tekstfil:
        tall=int(line)
        count+=1
        total+=tall
    tekstfil.close()
except ValueError:
    print('Fant en feil i filen:',line)


print('Sum total til feil i fil:',total,'Antall tall telt:',count)
