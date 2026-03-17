import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


autot = []


for i in range(10):
    rek = "ABC-" + str(i+1)
    huippu = random.randint(100, 200)
    autot.append(Auto(rek, huippu))


kilpailu = True

while kilpailu:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu = False


print("Rek  Huippu  Nopeus  Matka")
for auto in autot:
    print(auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.kuljettu_matka)