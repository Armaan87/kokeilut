def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

g = float(input("Anna gallonat: "))

while g >= 0:
    litrat = gallonat_litroiksi(g)
    print("Litraa:", litrat)
    g = float(input("Anna gallonat: "))
