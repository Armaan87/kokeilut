lentoasemat = {}
while True:
    valinta = input("Valitse: (uusi / hae / lopeta): ")

    if valinta == "uusi":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif valinta == "hae":
        icao = input("Anna ICAO-koodi: ")
        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Lentoasemaa ei löydy")
    elif valinta == "lopeta":
        break
