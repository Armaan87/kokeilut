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


# pääohjelma
auto = Auto("ABC-123", 142)

auto.kiihdyta(60)      # nopeus 60 km/h
auto.kulje(1.5)        # ajetaan 1.5 tuntia

print("Kuljettu matka:", auto.kuljettu_matka)