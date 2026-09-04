# mod 6 t2
#numbers = []

#while True:
    #input_number = input("Anna luku: ")

    #if input_number == "":
        # lopeta kysely
        #break

    # lisätään syötetty luku listalle
    #numbers.append(int(input_number))

#numbers.sort(reverse=True)

# quick'n'dirty
#print(numbers[0:5])

# for-lauseella viisi ensimmäistä alkiota
#for num in range(5):
    #print(numbers[num])


## mod6 Tehtävä 1

dice_amount = int(input("Kuinka monta arpakuutiota: "))

summa = 0

for num in range(dice_amount):
    noppa = random.randint(1, 6)
    summa = summa + noppa

print("Silmälukujen summa on:", summa)
