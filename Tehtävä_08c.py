import mysql.connector
from geopy.distance import geodesic

def hae_koordinaatit(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    return kursori.fetchone()


# Pääohjelma
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Armaan',
    password='Oparmaan06',
    autocommit=True
)

icao1 = input("Anna ensimmäinen ICAO-koodi: ")
icao2 = input("Anna toinen ICAO-koodi: ")

koord1 = hae_koordinaatit(icao1)
koord2 = hae_koordinaatit(icao2)

if koord1 and koord2:
    etaisyys = geodesic(koord1, koord2).kilometers
    print("Etäisyys:", round(etaisyys, 2), "km")
else:
    print("Toista kenttää ei löytynyt.")