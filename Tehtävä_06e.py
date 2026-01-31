def poista_parittomat(lista):
    uusi = []
    for luku in lista:
        if luku % 2 == 0:
            uusi.append(luku)
    return uusi

luvut = [1, 2, 3, 4, 5, 6, 7, 8]
karsittu = poista_parittomat(luvut)

print("Alkuperäinen:", luvut)
print("Karsittu:", karsittu)
