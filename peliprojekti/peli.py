import random
# PROJEKTI 1

nimi = input("Anna pelaajan nimi: ")
ikä = int(input("Anna pelaajan ikä: "))

print("Pelaajan nimi:", nimi)
print("Pelaajan ikä:", ikä)


# INVENTAARIO

inventaario = []


# FUNKTIOT

def pompi():
    korkeus = random.randint(1, 5)
    print("Pallo pomppasi", korkeus, "metriä korkealle!")
    return korkeus


def alas():
    print("Pallo tuli alas")


def näytä_inventaario(tavarat):
    print("Inventaario:")

    if len(tavarat) == 0:
        print("Inventaario on tyhjä")
    else:
        for esine in tavarat:
            print("-", esine)


def käytä_sydän(tavarat):
    if "sydän" in tavarat:
        tavarat.remove("sydän")
        print("Käytit sydämen!")
        print("Sait yhden elämän takaisin")
        return 1
    else:
        print("Sinulla ei ole sydäntä")
        return 0


def käytä_tähti(tavarat):
    if "tähti" in tavarat:
        tavarat.remove("tähti")
        print("Käytit kultaisen tähden!")
        print("Sait 5 bonuspistettä")
        return 5
    else:
        print("Sinulla ei ole tähteä")
        return 0


# PÄÄOHJELMA

if ikä < 12:
    print("Olet alaikäinen")
    print("Et pääse pelaamaan")

else:
    print("")
    print("Tervetuloa POMPPUPALLO-peliin", nimi)
    print("Tavoitteena on saada 30 pistettä")
    print("Sinulla on 3 elämää")
    print("Varo esteitä!")

    peli_käynnissä = True
    pisteet = 0
    hypyt = 0
    elämät = 3

    while peli_käynnissä:

        print("")
        print("====== POMPPUPALLO ======")
        print("Pisteet:", pisteet)
        print("Elämät:", elämät)
        print("Hypyt:", hypyt)
        print("")
        print("p = pompi")
        print("a = alas")
        print("i = inventaario")
        print("s = käytä sydän")
        print("t = käytä tähti")
        print("lopeta = lopeta peli")

        valinta = input("Anna komento: ")

        if valinta == "p":

            korkeus = pompi()

            pisteet += korkeus
            hypyt += 1

            print("Sait", korkeus, "pistettä")

            tapahtuma = random.randint(1, 6)

            if tapahtuma == 1:
                print("VARO!")
                print("Pallo osui piikkiin!")
                elämät -= 1
                print("Menetit yhden elämän")

            elif tapahtuma == 2:
                print("Löysit sydämen!")
                inventaario.append("sydän")

            elif tapahtuma == 3:
                print("Löysit kultaisen tähden!")
                inventaario.append("tähti")

            elif tapahtuma == 4:
                print("SUPERHYPPY!")
                print("Sait 5 bonuspistettä")
                pisteet += 5

            elif tapahtuma == 5:
                print("Pallo osui trampoliiniin!")
                print("Sait 3 bonuspistettä")
                pisteet += 3

            else:
                print("Turvallinen hyppy!")

            print("")
            print("Pisteitä yhteensä:", pisteet)
            print("Elämiä jäljellä:", elämät)

            if elämät <= 0:
                print("")
                print("GAME OVER!")
                print("Menetit kaikki elämäsi")
                print("Pisteitä tuli:", pisteet)
                print("Hyppyjä tuli:", hypyt)
                peli_käynnissä = False

            elif pisteet >= 30:
                print("")
                print("VOITIT PELIN!")
                print("Sait vähintään 30 pistettä")
                print("Pisteitä tuli:", pisteet)
                print("Hyppyjä tuli:", hypyt)
                peli_käynnissä = False


        elif valinta == "a":

            alas()

            if pisteet > 0:
                pisteet -= 1
                print("Menetit 1 pisteen")

            else:
                print("Sinulla ei ole pisteitä menetettäväksi")

            print("Pisteitä yhteensä:", pisteet)


        elif valinta == "i":

            näytä_inventaario(inventaario)


        elif valinta == "s":

            if elämät < 3:
                saatu_elämä = käytä_sydän(inventaario)
                elämät += saatu_elämä
            else:
                print("Sinulla on jo täydet elämät")

            print("Elämät:", elämät)


        elif valinta == "t":

            bonus = käytä_tähti(inventaario)
            pisteet += bonus

            print("Pisteet:", pisteet)

            if pisteet >= 30:
                print("")
                print("VOITIT PELIN!")
                print("Pisteitä tuli:", pisteet)
                print("Hyppyjä tuli:", hypyt)
                peli_käynnissä = False


        elif valinta == "lopeta":

            print("")
            print("Lopetit pelin")
            print("Pisteitä tuli:", pisteet)
            print("Hyppyjä tuli:", hypyt)
            print("Elämiä jäi:", elämät)

            peli_käynnissä = False


        else:
            print("Tuntematon komento")


