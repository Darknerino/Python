PESEL = input("Podaj pesel: ")

def czy_parzysta (pesel):
    parzysta = None
    if int(pesel[9]) % 2 == 1:
        print("M")
    elif int(pesel[9]) % 2 == 0:
        print("K")
    else:
        print("Niepoprawny pesel")

czy_parzysta(PESEL)
