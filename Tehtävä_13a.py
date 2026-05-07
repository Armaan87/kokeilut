from flask import Flask, jsonify

app = Flask(__name__)

def onko_alkuluku(luku):
    if luku < 2:
        return False
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            return False
    return True


@app.route('/alkuluku/<int:luku>')
def tarkista(luku):
    tulos = onko_alkuluku(luku)
    return jsonify({
        "Number": luku,
        "isPrime": tulos
    })

if __name__ == '__main__':
    app.run(port=3000)