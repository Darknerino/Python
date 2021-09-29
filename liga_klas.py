punkty = int(input("Podaj ilość punktów klasy: "))
frekwencja = int(input("Podaj frekwencje klasy: "))
srednia = float(input("Podaj srednia ocen klasy: "))

if frekwencja > 94 and srednia >= 4:
    punkty += 20
    print(f"Aktualna liczba punktów to: {punkty}")
elif frekwencja <= 94 or srednia < 4:
    print(f"Aktualna liczba punktów to: {punkty}")
else:
    print("Coś poszło nie tak")