# 1
for i in range(11):
    if i % 2 == 0:
        print(i)

print("\n")

# 2
i = 50
while i <= 150:
    print(i)
    i += 3

print("\n")

# 3
my_list = [5, 3, 10, 17, 4]
print(min(my_list))

print("\n")

# 4
for i in range(1, 11):
    print(i + i-1)

print("\n")

# 5
j = 1
while j < 8:
    if j == 5:
        print("Znalazłem 5!")
    else:
        print(j)
    j += 1

print("\n")

# 6
abc = ["a", "b", "c"]
for i in range(1, 4):
    for x in abc:
        print(str(i) + " " + x)

print("\n")

# 7 
for i in range(11, -1, -1):
    print(i)
print("Rakieta startuje!")

print("\n")

# 8
lista1 = ["KKKK", "GGGG", "HHHH"]
lista2 = ["563-12", "363-AB"]
for i in lista1:
    for j in lista2:
        print(i + " " + j)
