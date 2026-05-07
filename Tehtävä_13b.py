from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Yhteys tietokantaan
yhteys = mysql.connector.connect(
    host="localhost",
    user="root",          # vaihda tarvittaessa
    password="salasana",  # vaihda tarvittaessa
    database="flight_game"  # kurssin tietokanta
)

# Reitti: /kenttä/<icao>
@app.route('/kenttä/<icao>')
def hae_kentta(icao):
    kursori = yhteys.cursor()

    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()

    if tulos:
        return jsonify({
            "ICAO": icao,
            "Name": tulos[0],
            "Municipality": tulos[1]
        })
    else:
        return jsonify({"error": "Kenttää ei löytynyt"})

# Käynnistys
if __name__ == '__main__':
    app.run(port=3000)