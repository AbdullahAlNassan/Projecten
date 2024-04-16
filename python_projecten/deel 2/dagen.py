week_dagen = ('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag')

print("De weekdagen zijn:")
for d in range(7):
    print(week_dagen[d])


print("De werkdagen zijn:")
for i in range(5):
    print(week_dagen[i])

print("De weekenddagen zijn:")
for w in range(5, 7):
    print(week_dagen[w])

print("De weekdagen omgekeerd zijn:")
for od in range(6, 0, -1):
    print(week_dagen[od])

print("De werkdagen omgekeerd zijn:")
for owd in range(4, 0, -1):
    print(week_dagen[owd])

print("De weekenddagen omgekeerd zijn:")
for owdd in range(6, 4, -1):
    print(week_dagen[owdd])