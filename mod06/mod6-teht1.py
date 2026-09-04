import random

import random

# mod6 Tehtävä 1

dice_amount = int(input("Kuinka monta arpakuutiota: "))

summa = 0

for num in range(dice_amount):
    noppa = random.randint(1, 6)
    summa = summa + noppa

print("Silmälukujen summa on:", summa)