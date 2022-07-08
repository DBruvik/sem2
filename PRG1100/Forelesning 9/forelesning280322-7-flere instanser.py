#PRG1100-2022-flere instanser
#Flere objekter/instanser av samme klasse, her:
#"Kontoene til flere personer, Kari og Knut"

class BankKonto:
    def __init__(self,saldo):
        self.__saldo=saldo
    
    def innskudd(self,belop):
        self.__saldo=self.__saldo+belop
    
    def uttak(self,belop):
        if self.__saldo>=belop:
            self.__saldo=self.__saldo+belop
        else:
            print('Feil: ikke nok på konto')

    def hentSaldo(self):
        return self.__saldo

def main():
    saldo=float(input('Hva er saldoen på konto til Kari?'))

    karisKonto=BankKonto(saldo)

    saldo=float(input('Hva er saldoen på konto til knut?'))

    knutsKonto=BankKonto(saldo)

    belop=float(input('Hvor mye skal kari sette inn på konto?'))
    karisKonto.innskudd(belop)

    print('Saldoen på kontoen til kari er:',karisKonto.hentSaldo())

    belop=float(input('Hvor mye skal knut sette inn på konto? '))
    knutsKonto.innskudd(belop)

    print('Saldoen på kontoen til knut er: ',knutsKonto.hentSaldo())

    belop=float(input('Hvor mye skal Kari ta ut fra konto?'))
    karisKonto.uttak(belop)

    print('Saldoen på kontoen til kari er:',karisKonto.hentSaldo())

    belop=float(input('Hvor mye skal knut ta ut fra konto? '))
    knutsKonto.uttak(belop)

    print('Saldoen til kontoen til Knut er: ',knutsKonto.hentSaldo())

main()

