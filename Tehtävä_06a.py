import random

def heita_noppa():
    return random.randint(1, 6)

luku = 0
while luku != 6:
    luku = heita_noppa()
    print(luku)
