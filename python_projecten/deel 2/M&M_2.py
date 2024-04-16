import random

kleuren = ['rood', 'blauw', 'groen', 'geel', 'bruin']

aantal_MnMs = int(input("Hoeveel M&M's wil je toevoegen aan de zak? "))

zak_met_MnMs = {}



for _ in range(aantal_MnMs):
    kleur = random.choice(kleuren)
    if kleur not in zak_met_MnMs:
        zak_met_MnMs[kleur] = 1
    else:
        zak_met_MnMs[kleur] += 1


print("Zak met M&M's:")
for kleur, aantal in zak_met_MnMs.items():
    print(f'{kleur} : {aantal}')