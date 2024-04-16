import random
from fruitmand import fruitmand

aantal_keer = int(input("Geef het aantal keer op: "))

for _ in range(aantal_keer):
    gekozen_fruit = random.choice(fruitmand)
    print(gekozen_fruit['name'])