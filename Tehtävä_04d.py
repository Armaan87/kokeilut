import random
oikea = random.randint(1,10 )
arvaus=int(input("Arvaa luku (1–10):"))
while arvaus != oikea:
    if arvaus > oikea:
        print("Liian suuri arvaus")
    else:
        print("Liian pieni arvaus")

    arvaus = int(input("Arvaa luku (1–10): "))

print("Oikein")