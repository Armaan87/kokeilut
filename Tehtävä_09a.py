class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

auto = Auto("ABC-123", 142)

print("Rekisteritunnus:", auto.rekisteritunnus)
print("Huippunopeus:", auto.huippunopeus)
print("Nopeus:", auto.nopeus)
print("Kuljettu matka:", auto.kuljettu_matka)