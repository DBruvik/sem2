#PRG1100-2022-instansiering paramateroverføring
#Program for brukerbestemt antall mynkast og opptelling av antall Krone og Mynt
#objekt-orientert tilnærming, hvor klassens metoder håndterer egenskaper ved mynten
#og programlogikken/spillet ligger i main()

import random

class Mynt:
    def __init__(self,sideopp):
        self.sideopp=sideopp

    def kast(self):
        if random.randint(0,1)==0:
            self.sideopp='Krone'
        else:
            self.sideopp='Mynt'
        
    def hentSideopp(self):
        return self.sideopp

def main():
    antallKron=0
    antallMynt=0
    sideopp=input('Hvilken side på mynten er opp før første kast? ')

    minMynt=Mynt(sideopp)

    print('Før første kast er denne siden opp:',minMynt.hentSideopp())

    antallKast=int(input('Hvor mange ganger skal mynten kastes? '))

    for antallGanger in range (1,antallKast+1,1):
        minMynt.kast()
        print('Resultatet av kast nr',antallGanger,'ble',minMynt.hentSideopp())
        if minMynt.hentSideopp()=='Krone':
            antallKron=antallKron+1
        else:
            antallMynt=antallMynt+1
    print('Resultatet av forsøksrekka ble',antallKron,'Krone og',antallMynt,'Mynt')

main()