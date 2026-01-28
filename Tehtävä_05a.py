import random
n = int(input("Anna arpakuutioiden määrä: "))
summa = 0
for i in range(n):
    silmaluku = random.randint(1, 6)
    summa += silmaluku
print("Silmälukujen summa:", summa)
