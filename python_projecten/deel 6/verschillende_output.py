from bestand1 import verzamel_gegevens

gegevens_list = verzamel_gegevens()
for gegevens in gegevens_list:
    print(f'In {gegevens["woonplaats"]} woont de {gegevens["leeftijd"]} jarige {gegevens['naam']} ')