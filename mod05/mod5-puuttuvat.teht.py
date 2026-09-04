import random

# Tehtävä 2

tuumat = float(input("Anna tuumat: "))

while tuumat >= 0:
    cm = tuumat * 2.54
    print("Senttimetreinä:", cm)
    tuumat = float(input("Anna tuumat: "))


    # Tehtävä 3

luvut = []

syote = input("Anna luku: ")

while syote != "":
    luku = int(syote)
    luvut.append(luku)

    syote = input("Anna luku: ")

print("Pienin:", min(luvut))
print("Suurin:", max(luvut))


    # Tehtävä 5

yritys = 0

while yritys < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break

    yritys = yritys + 1

if yritys == 5:
    print("Pääsy evätty")