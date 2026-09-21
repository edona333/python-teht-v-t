import random


class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


class Kilpailu:

    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("Rekisteri | Huippunopeus | Nopeus | Kuljettu matka")

        for auto in self.autot:
            print(
                auto.rekisteritunnus, "|",
                auto.huippunopeus, "|",
                auto.nopeus, "|",
                auto.kuljettu_matka
            )

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True

        return False


autot = []

for i in range(10):
    rekisteritunnus = "ABC-" + str(i + 1)
    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1

    if tunnit % 10 == 0:
        print("Tilanne", tunnit, "tunnin jälkeen")
        kilpailu.tulosta_tilanne()


print("Kilpailu päättyi")
kilpailu.tulosta_tilanne()