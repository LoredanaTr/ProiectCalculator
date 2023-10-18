from calculators.calculatorABC import CalculatorABC


class CalculatorSimplu(CalculatorABC):

    def __init__(self, valoare_initiala=0):
        super().__init__(valoare_initiala) #apeleaza constructorul din clasa abstracta

    def calculate(self, operatia, numar):
        if operatia == '+':
            return self.adunare(numar)
        elif operatia == '-':
            return self.scadere(numar)
        elif operatia == '*':
            return self.inmultire(numar)
        elif operatia == '/':
            return self.impartire(numar)
        else:
            print('Operatie invalida.')
            return 0
    def adunare(self, numar):
        self.valoare_curenta += numar

    def scadere(self, numar):
        self.valoare_curenta -= numar

    def impartire(self, numar):
        if numar != 0:
            self.valoare_curenta /= numar
        else:
            print('Nu se poate efectua impartirea.')
            return 0

    def inmultire(self, numar):
        self.valoare_curenta *= numar




