import random

def heita_noppa(tahkot):
    return random.randint(1, tahkot)

max_luku = int(input("Anna nopan maksimisilmäluku: "))

luku = 0
while luku != max_luku:
    luku = heita_noppa(max_luku)
    print(luku)
