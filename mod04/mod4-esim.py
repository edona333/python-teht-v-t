

import random

# kolikonheittosimulaattori
random_number = random.randint(0, 1)
print(random_number)

if random_number == 0:
    result = "kruuna"
    print("kruuna tuli")
else:
    result = "klaava"

print(f"Heitit kolikkoa ja sait {result}.")


# boolean
onko_totta = False

if onko_totta:
    print("Onhan se totta!")
else:
    print("Ei ollut totta!")


## kolikonheittosimulaattori 2.0
# kolikko pystyyn tod.näk. oikeasti jotain 1/6000 luokkaa?

random_number = random.random()
print(random_number)  # liukulukuarvo väliltä 0-1

# kolikko jää pystyyn todennäköisyys 1/100
if random_number < 0.01:
    print("Kolikko jäi pystyyn")
elif random_number < 0.505:
    print("Kruuna tuli!")
else:
    print("Klaava tuli!")

## erilaisia ehtoja

arvo = 150

print(90 < arvo < 110)
print(100 != 10)


# kalvoesimerkki

ikä = int(input("Anna ikä: "))

if 15 <= ikä < 18:
    paino = float(input("Anna paino (kg): "))

if (ikä >= 18 or ikä >= 15 and paino >= 55):
    print("Lääkkeen käyttö on sallittua.")


# jälkimmäinen if-lause ikäarvolla 18
print(True or (True and False))

# esimerkki ehdoista (jälkimmäinen if-lause) ikäarvolla 18
#print(True or (True and False))

print(not True)