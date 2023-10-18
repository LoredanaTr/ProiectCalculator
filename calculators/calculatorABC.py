from abc import ABC, abstractmethod


class CalculatorABC(ABC):

    def __init__(self, valoare_initiala=0.0):
        self.valoare_curenta = valoare_initiala
    @abstractmethod
    def calculate(self):
        pass
