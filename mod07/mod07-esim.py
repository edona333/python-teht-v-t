# Mod 7 - Funktio tuntiesimerkkejä

print("print() on Pythonin sisäänrakennettu funktio")

def do_nothing():
    pass

do_nothing()

"""
def print_list_of_numbers():
    print(1)
    print(2)
    print(3)

print_list_of_numbers()
print_list_of_numbers()
"""

# Funktion parametrit (argumentit) ovat muuttujia, joiden arvot ovat käytössä
# funktion sisällä ja joille syötetään arvot funktiota kutsuttaessa
def print_list_of_numbers(start, end):
    print(f"Tulostettava väli: {start}, {end}")
    for i in range(start, end + 1, 1):
        print(i)
        

print_list_of_numbers(1, 5)
# funktio ilman return-sanaa tai pelkkä return-sana ilman määritetty paluuarvo 
test_return_value = print_list_of_numbers(7, 11)
print("test return value", test_return_value)

# Funktio ja paluuarvo (return)
print()
number = "01"
# int()-funktio palauttaa annetun parametrin arvon kokonaislukutyyppisenä
print(int(number)) # "01" => 1

# Funktio joka ei tulosta numeroita suoraan vaan palauttaa ne listamuodossa
def create_list_of_numbers(start, end):
    print(f"Tehdään lista, jossa arvot: {start}-{end}")
    number_list = []

    for i in range(start, end + 1, 1):
        number_list.append(i)

    return number_list

print(create_list_of_numbers(end=7, start=3))

list_of_numbers = create_list_of_numbers(11, 16)
#print(list_of_numbers)


# Lista parametrina (ks. materiaali)

def inventaario(tavarat):
    print("Sinulla on seuraavat tavarat:")
    for t in tavarat:
        print("- " + t)

    # Tavarat katoavat inventaariossa!
    tavarat.clear()
    return

reppu = ["Vesipullo", "Kartta", "Kompassi"]

inventaario(reppu)
reppu.append("Linkkuveitsi")
inventaario(reppu)

##########
### Vaihtuva määrä parametreja, käsitellään monikkona ( kuin lista)
print()

def summa(*luvut):
    print("Syötetyt arvot: ", luvut)
    s = 0
    for l in luvut:
        s += l

    return s

print("Summa on", summa(1, 1, 1, 1, 1, 1))






####
## Tehtäväesimerkkejä
import random

# T1 + T2
print("\n=== Noppapeli ===")

def heita_noppaa(tahkojen_lkm):
    return random.randint(1, tahkojen_lkm)

nopan_koko = int(input("Anna nopan koko (maksimisilmäluku): "))

silmaluku = 0
while silmaluku != nopan_koko:
    silmaluku = heita_noppaa(nopan_koko)
    print(silmaluku)


# TEHTÄVÄ 3

def gallonat_litroiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat


gallonat = float(input("Anna gallonamäärä: "))

while gallonat >= 0:
    litrat = gallonat_litroiksi(gallonat)
    print("Litroina:", litrat)

    gallonat = float(input("Anna gallonamäärä: "))



# TEHTÄVÄ 4

def summa(luvut):
    yhteensa = 0

    for luku in luvut:
        yhteensa += luku

    return yhteensa


luvut = [1, 2, 3, 4, 5]

tulos = summa(luvut)

print("Summa on:", tulos)



# Tehtävä 5

def parilliset(luvut):
    uusi_lista = []

    for luku in luvut:
        if luku % 2 == 0:
            uusi_lista.append(luku)

    return uusi_lista


alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8]

karsittu_lista = parilliset(alkuperainen_lista)

print("Alkuperäinen lista:", alkuperainen_lista)
print("Karsittu lista:", karsittu_lista)


