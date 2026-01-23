luku = input("Anna luku (tyhjä lopettaa):")
pienin = None
suurin = None
while luku != "":
    luku = float(luku)
    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku
    luku = input("Anna luku (tyhjä lopettaa): ")
print("Pienin:", pienin)
print("Suurin:", suurin)

