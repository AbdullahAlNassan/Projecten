import random

def vraag_gegevens():
    gegevens = {}

    naam = input('Wat is je naam? ')
    leeftijd = input('Hoe oud ben je? ')
    haar_kleur = input('wat voor kleur haar heb je?')

    gegevens["naam"] = naam
    gegevens['leeftijd'] = leeftijd
    gegevens['kleur'] = haar_kleur
    
    return gegevens

def verzamel_gegevens():
    gegevens_list = []
    while True:
        stoppen = input('klick enter om door te gaan of toets stop om te stoppen: ')
        if stoppen == 'stop':
            break
        gegevens = vraag_gegevens()
        gegevens_list.append((gegevens))
    return gegevens_list

