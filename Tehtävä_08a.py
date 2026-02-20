import mysql.connector

def hae_kentan_tiedot(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{icao}'"
    print(sql)

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentoaseman nimi on {rivi[0]}")
            print(f"Sijaintikunta on {rivi[1]}")
    else:
        print("ICAO-koodilla ei löytynyt lentoasemaa.")
    return

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Armaan',
    password='Oparmaan06',
    autocommit=True
)

icao_koodi = input("Anna kentän ICAO-koodi: ")
hae_kentan_tiedot(icao_koodi)