from fruitmand import fruitmand

watermeloen = {
    'name': 'watermeloen',
    'weight': 5000,
    'color': 'green',
    'round': True
}

fruitmand.append(watermeloen)

for fruit in fruitmand:
    if fruit['name'] != 'watermeloen':
        print(fruit['weight'])