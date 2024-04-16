from fruitmand import fruitmand

while True:
    gekozen_kleur = input("Kies een kleur uit de fruitmand: ")

    kleur_gevonden = False

    for fruit in fruitmand:
        if fruit['color'] == gekozen_kleur:
            kleur_gevonden = True
            
    if kleur_gevonden:
        break
    else:
        print(f"De kleur {gekozen_kleur} zit er niet in de fruitmand. Probeer opnieuw.")


ronde_vruchten = 0
niet_ronde_vruchten = 0

for fruit in fruitmand:
    if fruit['color'] == gekozen_kleur:
        if fruit['round']:
            ronde_vruchten += 1
        else:
            niet_ronde_vruchten += 1

verschil = ronde_vruchten - niet_ronde_vruchten

if ronde_vruchten > niet_ronde_vruchten:
    print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")
elif ronde_vruchten < niet_ronde_vruchten:
    print(f"Er zijn {verschil} minder ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")
else:
    print(f"Er zijn {ronde_vruchten} ronde vruchten en {niet_ronde_vruchten} niet ronde vruchten in de kleur {gekozen_kleur}")


