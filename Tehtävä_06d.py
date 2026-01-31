def summa(lista):
    s = 0
    for luku in lista:
        s += luku
    return s

luvut = [1, 2, 3, 4, 5]
tulos = summa(luvut)
print("Summa:", tulos)
