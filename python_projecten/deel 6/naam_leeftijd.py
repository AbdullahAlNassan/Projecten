def vraag_naam_leeftijd():
    gegevens = {}
    naam = input('Wat is je naam? ')
    age = input('Hoe oud ben je? ')
    kleur_haar = input('wat is je haar kleur?')

    gegevens["naam"] = naam
    gegevens['leeftijd'] = age
    gegevens['kleur'] = kleur_haar
    
    return gegevens

gegevens = vraag_naam_leeftijd()
print(f'{gegevens["naam"]} is {gegevens["leeftijd"]} jaar en heeft {gegevens["kleur"]} haar!')