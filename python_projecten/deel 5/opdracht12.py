from fruitmand import fruitmand

kleuren_vertaling = {
    'yellow': 'geel',
    'green': 'groen',
    'orange': 'oranje',
    'red': 'rood',
    'brown': 'bruin'
}

langste_naam_fruit = fruitmand[0]

for fruit in fruitmand:
    if len(fruit['name']) > len(langste_naam_fruit['name']):
        langste_naam_fruit = fruit


fruit_naam = langste_naam_fruit['name']
fruit_kleur = kleuren_vertaling.get(langste_naam_fruit['color'])
fruit_gewicht = langste_naam_fruit['weight']

print(f'De "{fruit_naam}" ({len(fruit_naam)} letters) heeft een {fruit_kleur} kleur en een gewicht van {fruit_gewicht} kg')