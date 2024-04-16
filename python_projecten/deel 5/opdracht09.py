from fruitmand import fruitmand

lijst = []

for fruit in fruitmand:
    if fruit["color"] not in lijst:
        lijst.append(fruit["color"])

print(lijst)

for _ in range(2):
    druif_index = None

    for index in range(len(fruitmand)):
        if fruitmand[index] ["name"] == "druif":
            druif_index = index
            
    fruitmand.pop(druif_index)


# index = 0

# while index < len(fruitmand):
#     if fruitmand[index]['name'] == 'druif':
#         fruitmand.pop(index)
#     else:
#         index += 1

for fruit in fruitmand:
    print(fruit)





