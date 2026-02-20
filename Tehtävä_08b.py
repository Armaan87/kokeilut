import mysql.connector

def hae_maara(maakoodi):
    sql = f"""
    SELECT type, COUNT(*)
    FROM airport
    WHERE iso_country='{maakoodi}'
    GROUP BY type
    """
    print(sql)

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"{rivi[0]}: {rivi[1]} kpl")
    else:
        print("Maakoodilla ei löytynyt lentoasemia.")
    return

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Armaan',
    password='Oparmaan06',
    autocommit=True
)

maa = input("Anna maakoodi (esim FI): ")
hae_maara(maa)