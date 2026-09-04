import random

# mod6 tehtävä 3

luku = int(input("Anna kokonaisluku: "))

alkuluku = True

for jakaja in range(2, luku):
    if luku % jakaja == 0:
        alkuluku = False

if alkuluku == True:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")