



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

