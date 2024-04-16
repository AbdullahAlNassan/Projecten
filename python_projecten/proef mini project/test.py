# import random

# unique_values = set()

# while True:
#     deelnemer = input("Voer een naam in: ")

#     if deelnemer in unique_values:
#         print("Waarde is niet uniek. Probeer het opnieuw.")
#     else:
#         unique_values.add(deelnemer)
#         print("Waarde succesvol toegevoegd.")

#     if len(unique_values) >= 3:
#         meer_namen = input("Wil je meer namen toevoegen? (ja of nee) ")
#         if meer_namen == "nee":
#             break

# deelnemers = list(unique_values)
# lootjes = list(deelnemers)
# random.shuffle(lootjes)

# niemand_heeft_zijn_eigen_lootje = True
# for i in range(len(deelnemers)):
#     if deelnemers[i] == lootjes[i]:
#         niemand_heeft_zijn_eigen_lootje = False
#         break

# if not niemand_heeft_zijn_eigen_lootje:
#     print("Herstart het programma en probeer opnieuw.")
# else:
#     for i in range(len(deelnemers)):
#         print(f"{deelnemers[i]} koopt voor: {lootjes[(i + 1) % len(deelnemers)]}")

import random

deelnemers = []

while True:
    deelnemer = input("Voer een naam in: ")

    if deelnemer in deelnemers:
        print("Waarde is niet uniek. Probeer het opnieuw.")
    else:
        deelnemers.append(deelnemer)
        print("Waarde succesvol toegevoegd.")

    if len(deelnemers) >= 3:
        meer_namen = input("Wil je meer namen toevoegen? (ja of nee) ")
        if meer_namen == "nee":
            break

lootjes = deelnemers[1:] + deelnemers[:1]  # Dit is de "cirkelvormige rotatie"

for i in range(len(deelnemers)):
    print(f"{deelnemers[i]} koopt voor: {lootjes[i]}")


