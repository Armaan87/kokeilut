luvut = []
luku = input("Anna luku (tyhjä lopettaa): ")
while luku != "":
    luvut.append(int(luku))
    luku = input("Anna luku (tyhjä lopettaa): ")
luvut.sort(reverse=True)
print("Viisi suurinta:", luvut[:5])
