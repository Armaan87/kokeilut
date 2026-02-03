nimet = set()
nimi = input("Anna nimi (tyhjä lopettaa): ")
while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)
    nimi = input("Anna nimi (tyhjä lopettaa): ")
for n in nimet:
    print(n)
