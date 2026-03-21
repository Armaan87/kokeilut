class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylos(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print("Nyt kerroksessa:", self.kerros)

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print("Nyt kerroksessa:", self.kerros)

    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde:
            self.kerros_ylos()
        while self.kerros > kohde:
            self.kerros_alas()


class Talo:
    def __init__(self, alin, ylin, hissien_maara):
        self.alin = alin
        self.hissit = []

        for i in range(hissien_maara):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissia(self, numero, kohde):
        self.hissit[numero].siirry_kerrokseen(kohde)

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)



talo = Talo(1, 10, 3)

talo.aja_hissia(0, 5)
talo.aja_hissia(1, 8)

print("Palohälytys!")
talo.palohalytys()