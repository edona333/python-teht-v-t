# Tehtävä 1

vuodenajat = ("talvi", "kevät", "kesä", "syksy")

kuukausi = int(input("Anna kuukauden numero: "))

if kuukausi == 12 or kuukausi == 1 or kuukausi == 2:
    print(vuodenajat[0])

elif kuukausi == 3 or kuukausi == 4 or kuukausi == 5:
    print(vuodenajat[1])

elif kuukausi == 6 or kuukausi == 7 or kuukausi == 8:
    print(vuodenajat[2])

elif kuukausi == 9 or kuukausi == 10 or kuukausi == 11:
    print(vuodenajat[3])

else:
    print("Virheellinen kuukauden numero")


# Tehtävä 2

nimet = set()

while True:
    nimi = input("Anna nimi: ")

    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("Syötetyt nimet:")

for nimi in nimet:
    print(nimi)



# Tehtävä 3

lentoasemat = {}

while True:
    toiminto = input("Valitse toiminto (uusi, hae, lopeta): ")

    if toiminto == "uusi":
        icao = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")

        lentoasemat[icao] = nimi
        print("Lentoasema lisätty")

    elif toiminto == "hae":
        icao = input("Anna ICAO-koodi: ")

        if icao in lentoasemat:
            print("Lentoaseman nimi:", lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt")

    elif toiminto == "lopeta":
        print("Ohjelma lopetetaan")
        break

    else:
        print("Tuntematon toiminto")