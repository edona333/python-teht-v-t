nimi = input("Anna pelaajan nimi: ")
ikä = int(input("Anna pelaajan ikä: "))

print("Pelaajan nimi:", nimi)
print("Pelaajan ikä:", ikä)

if ikä < 12:
    print("Olet liian nuori pelaamaan")

else:
    peli_käynnissä = True

    print("Tervetuloa peliin", nimi)

    while peli_käynnissä:
        print("p = pompi")
        print("a = alas")
        print("l = lopeta")

        valinta = input("Anna komento: ")

        if valinta == "p":
            print("Pallo pomppii ylös")

        elif valinta == "a":
            print("Pallo tulee alas")

        elif valinta == "l":
            print("Lopetit pelin")
            peli_käynnissä = False
            break

        else:
            print("Virheellinen komento")