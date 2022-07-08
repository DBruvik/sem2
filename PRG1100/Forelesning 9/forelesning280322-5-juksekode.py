#PRG1100-2022-juksekode
#Program for brukerbestemt antall myntkast og opptelling av antall Krone og Mynt
#Objekt-orientert tilnørming, hvor klassens metoder håndterere egenskapen ved mynten
#og programlogikken/spillet ligger i main()

#Introduksjon til private/skjulte attributter
#Vi bør sikre oss at det bare er metodene til objektet som kan endre aksessere attributtene
#/instansevariablene
#Slik det er nå kan kode i main endre verdier på attributter til objektet/dvs "jukse i spillet"

import random

#Mynt-klassen simulerere en mynt og hva en kan gjøre med den
class Mynt:
    #__init__ metoden initierer objektet/forekomsten/instansen
    #og tilordner sideopp-attributtet (self.sideopp) startverdi via en input i __init__
    #dvs setter en startverdi som ikke skal telles med
    def __init__(self):
        #Oppgave "myntside" opp før første kast
        self.sideopp=input('Hvilken side på mynten er opp før første kast? ')

    #kast metoden simulerer ett kast med mynten
    #og gir sideopp-attributter ny verdi
    def kast(self):
        if random.randint(0,1)==0:
            self.sideopp='Krone'
        else:
            self.sideopp='Mynt'

    #hentSideopp metoden returnerer til enhver tid
    #verdien/("siste verdi") på mynten, dvs sideopp-attributtet
    def hentSideopp(self):
        return self.sideopp
def main():
    antallKron=0
    antallMynt=0

    #Oppretter et mynt-objekt, en forekomst/instanse
    minMynt=Mynt()
    print('Før første kast er denne siden opp:',minMynt.hentSideopp())
    antallKast=int(input('Hvor mange ganger skal mynten kastes? '))
    for antallGanger in range(1,antallKast+1,1):
        #Mynten kastes
        minMynt.kast()

        #Resultatet av kastet skrives ut
        print('Resultatet av kast nr',antallGanger,'ble',minMynt.hentSideopp())

        #Her kommer den nye "jukse-koden"
        #Uansett hva som blir resultatet av kast-metode oversturer vi 
        #resultatet til å bli f eks Krone
        minMynt.sideopp='Krone'
        print('Resultatet av kast nr',antallGanger,'ble manipulert til',minMynt.hentSideopp())
        print()

        #Opptelling gjennomføres
        if minMynt.hentSideopp()=='Krone':
            antallKron=antallKron+1
        else:
            antallMynt=antallMynt+1
    print('Resultatet av forsøksrekka ble',antallKron,'Krone og',antallMynt,'Mynt')

main()

