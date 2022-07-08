#PRG1100-2022-private atributter

#Program for brukerbestemt antall myntkast og opptelling av antall Krone og Mynt
#objekt-orientert tilnærming, hvor klassens metoder håndterer egenskaper ved mynten
#og programlogikken/spillet ligger i main()

#For å sikre oss at annen kode ikke kan endre/korruptere verdier på objektets
#data-attributter/instansevariabler
#gjør vi attributtene private, dvs at det bare er objektets metoder som har
#direkte aksess/tilgang til data-attributtene
#I python gjøres det ved å starte attributt-navnet med 2 _, dvs __

import random

class Mynt:
    def __init__(self):
        self.__sideopp=input('Hvilken side på mynten er opp før første kast? ')

    def kast(self):
        if random.randint(0,1)==0:
            self.__sideopp='Krone'
        else:
            self.__sideopp='Mynt'

    def hentSideopp(self):
        return self.__sideopp

def main():
    antallKron=0
    antallMynt=0
    minMynt=Mynt()

    print('Før første kast er denne siden opp:',minMynt.hentSideopp())

    antallKast=int(input('Hvor mange ganger skal mynten kastes? '))

    for antallGanger in range(1,antallKast+1,1):
        minMynt.kast()

        print('Resultatet av kast nr',antallGanger,'ble',minMynt.hentSideopp())
        minMynt.__sideopp='Krone'
        print('Resultatet av kast nr',antallGanger,'ble forsøkt manipulert men hindret',minMynt.hentSideopp())
        print()

        if minMynt.hentSideopp()=='Krone':
            antallKron=antallKron+1
        else:
            antallMynt=antallMynt+1
    print('Resultatet av forsøksrekka ble',antallKron,'Krone og',antallMynt,'Mynt')

main()