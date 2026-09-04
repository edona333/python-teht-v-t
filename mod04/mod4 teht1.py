# 4. Valintarakenne (if) tehtävä 1

pituus = float(input("Syötä kuhan pituus senttimetreinä: "))

if pituus < 37:
    puuttuu = 37 - pituus
    print("Kuha on alamittainen. Laske kuha takaisin järveen.")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu} cm.")
else:
    print("Kuha täyttää sallitun pyyntimitan.")


### tehtävä 3###

sukupuoli = input("Anna sukupuoli (nainen/mies): ")
hemoglobiini = int(input("Anna hemoglobiiniarvo: "))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiini on alhainen")
    elif hemoglobiini <= 175:
        print("Hemoglobiini on normaali")
    else:
        print("Hemoglobiini on korkea")

elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiini on alhainen")
    elif hemoglobiini <= 195:
        print("Hemoglobiini on normaali")
    else:
        print("Hemoglobiini on korkea")

else:
    print("Virheellinen sukupuoli")


    ### Tehtävä 4 ####

vuosi = int(input("Anna vuosiluku: "))

if vuosi % 400 == 0:
    print("Vuosi on karkausvuosi")

elif vuosi % 100 == 0:
    print("Vuosi ei ole karkausvuosi")

elif vuosi % 4 == 0:
    print("Vuosi on karkausvuosi")

else:
    print("Vuosi ei ole karkausvuosi")