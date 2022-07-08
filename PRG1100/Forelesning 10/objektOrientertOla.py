#Oppgave 4

class Kunde:
    def __init__(self,mobilnr,fornavn,etternavn,epost):
        #initialiserer variablene
        self.__mobilnr=mobilnr
        self.__fornavn=fornavn
        self.__etternavn=etternavn
        self.__epost=epost

    def set_epost(self,epost):
        self.__epost=epost

    def get_epost(self):
        return self.__epost


def main():
    kunde1=Kunde('98989898','Daniel','Bruvik','daniel_bruvik@hotmail.com')

    #Om du skal endre eposten
    kunde1.set_epost('bruvik@hotmail.com')



#Oppgave 5
import kunde
import pickle

def les_fil():
    fortsett=True
    kundefil=open("Kunde.dat","rb")

    while fortsett==True:
        try:
            kunde=pickle.load(kundefil)

            print('Mobilnummer:',kunde.get_mobilnr())
            print('Etternavn:',kunde.get_etternavn())
            print('E-post:',kunde.get_epost())

        except EOFError:
            fortsett=False
    kundefil.close()

les_fil()
