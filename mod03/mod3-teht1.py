import math
import random



# Tehtävä 1

nimi = input("Anna nimesi: ")
print("Terve, " + nimi + "!")




# Tehtävä 2

r = float(input("Anna säde niin lasken ympyrän pinta-alan: "))
A = math.pi * r ** 2
print(f"Ympyrän pinta-ala on {A:.2f} yksikköä")




# Tehtävä 3

a = float(input("Anna suorakulmion kanta: "))
b = float(input("Anna suorakulmion korkeus: "))

p = 2 * (a + b)
A = a * b

print(f"Suorakulmion piiri on {p:.2f}")
print(f"Suorakulmion pinta-ala on {A:.2f}")

# Tehtävä5
leiviskat_lkm = int(input("Anna leivisköjen määrä: "))
naulat_lkm = int(input("Anna naulojen määrä: "))
luodit_lkm = float(input("Anna luotien määrä: "))

# Lasketaan leiviskät mukaan nauloihin
naulat_lkm = leiviskat_lkm * 20 + naulat_lkm

# Lasketaan naulat mukaan luoteihin
luodit_lkm = naulat_lkm * 32 + luodit_lkm

# Muutetaan luodit grammoiksi
massa_g = luodit_lkm * 13.3

# Kilot ja jäljelle jäävät grammat
kilot = int(massa_g // 1000)
grammat = massa_g % 1000

print(f"Massa nykymittojen mukaan: {int(massa_g // 1000)} kiloa ja {massa_g % 1000:.2f} grammaa.")



# Tehtävä 6

luku = random.randint(0, 9)
luku2 = random.randint(0, 9)
luku3 = random.randint(0, 9)

print(f"{luku} {luku2} {luku3}")
print(f"{random.randint(0, 9)} {random.randint(0, 9)} {random.randint(0, 9)}")