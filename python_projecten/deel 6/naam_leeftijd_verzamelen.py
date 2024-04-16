from naam_leeftijd import vraag_naam_leeftijd

# def vraag_gegevens():
#     gegevens = {}

#     naam = input('Wat is je naam? ')
#     leeftijd = input('Hoe oud ben je? ')

#     gegevens["naam"] = naam
#     gegevens['leeftijd'] = leeftijd
    
#     return gegevens

def verzamel_gegevens():
    gegevens_list = []
    while True:
        stoppen = input('klick enter om door te gaan of toets stop om te stoppen: ')
        if stoppen == 'stop':
            break
        gegevens = vraag_naam_leeftijd()
        gegevens_list.append((gegevens))
    return gegevens_list

gegevens_list = verzamel_gegevens()
for gegevens in gegevens_list:
    print(f'{gegevens["naam"]} is {gegevens["leeftijd"]} jaar')


