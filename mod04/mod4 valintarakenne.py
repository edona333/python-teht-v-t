# 4. Valintarakenne (if) tehtävä 1

pituus = float(input("Syötä kuhan pituus senttimetreinä: "))

if pituus < 37:
    puuttuu = 37 - pituus
    print("Kuha on alamittainen. Laske kuha takaisin järveen.")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu} cm.")
else:
    print("Kuha täyttää sallitun pyyntimitan.")