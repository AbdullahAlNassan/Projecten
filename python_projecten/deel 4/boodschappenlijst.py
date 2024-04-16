boodschappenlijst = {}

while True:
    item = input("Voer het item in: ").lower()
    hoeveelheid = int(input("Voer de hoeveelheid in: "))

    if item in boodschappenlijst:
        boodschappenlijst[item] += hoeveelheid
    else:
        boodschappenlijst[item] = hoeveelheid

    meer_toevoegen = input("Wil je meer items toevoegen? (ja/nee): ")

    if meer_toevoegen.lower() != "ja":
        break

print("[BOODSCHAPPENLIJST]")
for item, hoeveelheid in boodschappenlijst.items():
    print(f"{hoeveelheid}x {item}")
