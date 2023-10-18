from calculators.calculatorABC import CalculatorABC


class CalculatorAdvance(CalculatorABC):
    def __init__(self, valoare_initiala=0):
        super().__init__(valoare_initiala)

    def calculate(self, operatia, numar, exponent):
        if operatia == '&':
            return self.modulo(numar)
        elif operatia == '**':
            return self.ridicare_la_putere(exponent)
        else:
            print('Operatie invalida.')
            return 0

    def ridicare_la_putere(self, exponent):
        self.valoare_curenta **= exponent

    def modulo(self, numar):
        self.valoare_curenta &= numar




