from calculators.calculator_simplu import CalculatorSimplu
from calculators.calculator_advance import CalculatorAdvance


#rezultat = None
def main():

    while True:
        print('Selecteaza calculatorul dorit')
        print('1. Calculator simplu')
        print('2. Calculator avansat')
        print('3. Exit')
        alegerea = input("Te rog alege intre 1, 2 si 3: ")

        #global rezultat #face variabile ce pot fi folosite ulterior in cod

        if alegerea == '1':
            rezultat = float(input("Introdu valoarea initiala: "))
            calculator_simplu = CalculatorSimplu(rezultat)
            operatie = input("te rog introdu operatia dorita: +, -, *, /: ")
            numar = float(input("Introdu numarul: \n"))
            while rezultat is not None:
                if operatie == '+':
                    rezultat = calculator_simplu.calculate(operatie, numar)
                    print(f"Rezultatul operatiei de adunare este: {rezultat}")
                elif operatie == '-':
                    rezultat = calculator_simplu.calculate(operatie, numar)
                    print(f"Rezultatul operatiei de scadere este: {rezultat}")
                elif operatie == '*':
                    rezultat = calculator_simplu.calculate(operatie, numar)
                    print(f"Rezultatul operatiei de inmultire este: {rezultat}")
                elif operatie == '/':
                    rezultat = calculator_simplu.calculate(operatie, numar)
                    print(f"Rezultatul operatiei de impartire este: {rezultat}")

        if alegerea == '2':
            rezultat = float(input("Introdu valoarea initiala: "))
            calculator_advance = CalculatorAdvance(rezultat)
            operatie = input("te rog introdu operatia dorita: &, **: ")
            numar = float(input("Introdu numarul: \n"))
            while rezultat is not None:
                if operatie == '&':
                    rezultat = calculator_advance.calculate(operatie, numar)
                    print(f"Rezultatul operatiei de modulo este: {rezultat}")
                elif operatie == '**':
                    exponent = float(input("Introdu exponentul: "))
                    rezultat = calculator_advance.calculate(operatie, numar, exponent)
                    print(f"Rezultatul operatiei de ridicare la putere este: {rezultat}")
        if alegerea == '3':
            print("Iesire din calculator")
            break


if __name__ == '__main__':
    main()

