#PRG110-2022-opptelling mynkast pp

#Program for brukerbestemt antall myntkast og opptelling av antall krone og myne
#Fuksjonsorientert/prosedural tilnærming

import random
antallKron=0
antallMynt=0
antallKast=int(input("Hvor mange ganger skal mynten kastes?"))

for antallGanger in range(1,antallKast+1,1):
    if random.randint(0,1)==0:
        sideopp='Krone'
        antallKron=antallKron+1
    else:
        sideopp='Mynt'
        antallMynt=antallMynt+1
    print('Resultatet av kast nr',antallGanger,'ble',sideopp)
print('Resultatet av forsøksrekka ble',antallKron,'Krone og',antallMynt,'Mynt')

