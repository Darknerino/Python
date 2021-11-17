def zadanie1 (liczba):
    lista = []
    for i in range(1, liczba+1):
        lista.append(liczba * i)
        print(lista[i-1])

# zadanie1(5)

def zadanie2 (x, y):
    lista = []
    for i in range(x, y):
        if i % 2 == 0:
            lista.append(i)

    print(lista)

# zadanie2(10, 18)

def zadanie3 (x, y):
    lista = []
    for i in range(x, y):
        if i % 2 == 1:
            lista.append(i)

    print(lista[::-1])

# zadanie3(9, 19)

def zadanie4 (x):
    lista = []
    for i in range(1, x+1):
        if x > 1:
            lista.append(i*i)
        else:
            pass

    print(lista)

# zadanie4(5)

def zadanie5 (x):
    lista = []
    for i in range(x, 0, -1):
        if x % i == 0:
            lista.append(i)

    print(lista)

zadanie5(25)
