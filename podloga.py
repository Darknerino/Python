a = float(input("Podaj dlugosc podlogi: "))
b = float(input("Podaj szerokosc podlogi: "))
p = float(input("Na ile m^2 przypada jedna paczka?: "))

wynik = (a*b)//p + 1

print("Ilosc paczek potrzebnych do ulozenia podlogi to " + str(wynik))