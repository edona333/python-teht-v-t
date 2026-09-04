import random

# Mod 5 tehtävä 6 aloitus ja idea
# pi=4n/N, jossa n on ympyrän sisään osuvat pisteet ja N kaikki arvotut pisteet
# Piste on ympyrän sisällä, jos x^2+y^2<1

N = int(input("Kuinka monta pistettä arvotaan: "))
n = 0
counter = 0

while counter < N:
    counter += 1

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    print(f"{counter}. arvotun pisteen koordinaatit, x: {x}, y: {y}")

    if x * x + y * y < 1:
        n = n + 1
        print("Piste on ympyrän sisällä.")

print(f"Pisteitä arvottu yhteensä {N}, joista ympyrän sisälle osui {n} kpl.")

pi = 4 * n / N
print("Piin likiarvo on:", pi)