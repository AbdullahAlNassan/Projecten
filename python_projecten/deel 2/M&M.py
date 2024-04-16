import random

kleuren = ('oranje', 'blauw', 'groen', 'bruin')

aantal_MMs = int(input("Hoeveel M&M's wil je aan de zak toevoegen? "))

def vul_zak_met_MMs(aantal):
    zak = []
    for _ in range(aantal):
        random_kleur = random.choice(kleuren)
        zak.append(random_kleur)
    return zak

zak_met_MMs = vul_zak_met_MMs(aantal_MMs)

print("Inhoud van de zak met M&M's:")
print(zak_met_MMs)

