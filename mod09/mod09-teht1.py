import random
class Auto:

    # rekisteritunnus, huippunopeus, tämänhetkinen nopeus
    # ja kuljettu matka

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        # self.nopeus = self.nopeus + muutos
        self.nopeus += muutos

        # Auton nopeus ei saa kasvaa huippunopeutta
        # suuremmaksi eikä alentua nollaa pienemmäksi
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

        # auto.kulje(1.5)


def moikka():
    print("Tämäpä on mukavaa")


auto = Auto("ABC-123", 142)

print("Auton rekisteritunnus:", auto.rekisteritunnus)
print("Huippunopeus:", auto.huippunopeus)
print("Nopeus:", auto.nopeus)
print("Kuljettu matka:", auto.kuljettu_matka)

# KIIHDYTÄ!!!!!!!!!!
moikka()

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print("Auton nopeus kiihdytyksen jälkeen:", auto.nopeus)

auto.kulje(1.5)

print("Kuljettu matka 1.5h jälkeen on:", auto.kuljettu_matka)

auto.kiihdytä(-200)

print("Auton nopeus jarrutuksen jälkeen:", auto.nopeus)


# TEHTÄVÄ 4

autot = []

for i in range(10):
    rekisteritunnus = "ABC-" + str(i + 1)
    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)


kilpailu_käynnissä = True

while kilpailu_käynnissä:

    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)

        auto.kiihdytä(nopeuden_muutos)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu_käynnissä = False


print("Kilpailu päättyi")

print("Rekisteri | Huippunopeus | Nopeus | Kuljettu matka")

for auto in autot:
    print(auto.rekisteritunnus, "|",
          auto.huippunopeus, "|",
          auto.nopeus, "|",
          auto.kuljettu_matka)